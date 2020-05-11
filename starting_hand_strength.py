from basic_items import card_items
import guts
import importlib
importlib.reload(guts)
import random as r
import json
import numpy as np

# Run a simulation to get the strength of the 169 starting hands
# Save the starting hand strengths as json files

class StartingHands:
    hand_ops = guts.HandOperations()
    starting_hands = card_items['starting_hands']
    full_deck = card_items['full_deck_of_cards']

    # This function takes a current deck of cards (need not be all 52 cards) and a number, and deals
    # that many cards out of the deck
    # Args:
    #   n_cards: Integer in [1,x-1] where x is the length of current_deck
    #   current_deck: List of n in [2, 52] cards
    # Output:
    #   dealt_cards: List of cards of length n_cards
    #   current_deck: List of cards of length x - n_cards

    def deal_cards(self, n_cards, current_deck):
        dealt_cards = r.sample(current_deck, n_cards)
        current_deck = [c for c in current_deck if c not in dealt_cards]
        return dealt_cards, current_deck

    # Converts a hand from the starting hand format to the regular format.
    # Args: a single dict object with keys
    #   'card_1': [rank]
    #   'card_2': [rank]
    #   'suited': [True or False]
    # Output: a list of two dict objects in the standard format

    def convert_hand_two_dicts(self, one_dict_hand):
        card_1 = one_dict_hand['card_1']
        card_2 = one_dict_hand['card_2']

        # Declare the actual 2 cards that consist the hand
        if one_dict_hand['suited']:
            # The particular suits don't matter because of symmetry
            my_hand = [{'rank': card_1, 'suit': 'hearts'},
                       {'rank': card_2, 'suit': 'hearts'}]
        else:
            my_hand = [{'rank': card_1, 'suit': 'hearts'},
                       {'rank': card_2, 'suit': 'diamonds'}]
        return my_hand

    # The inverse of convert_hand_two_dicts

    def convert_hand_one_dict(self, two_dict_hand):
        card_1 = two_dict_hand['rank']
        card_2 = two_dict_hand['rank']
        suited = self.hand_ops.is_suited(two_dict_hand)
        return {'card_1': card_1, 'card_2': card_2, 'suited': suited}

    # This function run n_sims simulations for any hand and table size and returns the number of times the hand wins
    # Args:
    #   my_hand: a list containing two dictionary objects of the format:
    #   n_sims: the number of simulations
    #   n_players: the number of players at the table
    # Output:
    #   wins: a float representing the number of times my_hand wins out of n_sims simulations. Split pots could as fractional wins

    def simulate_hands(self, hand_to_simulate, num_sims, num_players):
        full_deck_minus_my_hand = [i for i in self.full_deck if i not in hand_to_simulate]
        rest_of_cards = full_deck_minus_my_hand
        assert len(rest_of_cards) == 50
        wins = 0
        for b in range(num_sims):
            if b % 1000 == 0 and b > 0:
                print('Sim number ', b)
            all_hands = [hand_to_simulate]  # This list of lists of dicts will hold all hands of the players at the table
            # Now deal the rest of the hands at the table, and add each hand to all_hands
            for j in range(num_players - 1):
                opponent_hand, rest_of_cards = self.deal_cards(2, rest_of_cards)
                all_hands.append(opponent_hand)
                assert len(rest_of_cards) == (50 - 2 * (j + 1))
            # Deal 5 table cards
            table_cards, rest_of_cards = self.deal_cards(5, rest_of_cards)
            assert len(rest_of_cards) == 52 - 2 * num_players - 5
            # Find the winning hands
            winners = self.hand_ops.get_winning_hands(all_hands, table_cards)
            winning_hands = winners['winners']
            if hand_to_simulate in winning_hands:
                wins += 1 / len(winning_hands)  # Splits are shared equally
            # Reset rest_of_cards
            rest_of_cards = full_deck_minus_my_hand
        return wins

    # This function determines the strength of each starting hand by simulation. It assumes opponents will never
    # fold
    # Args:
    #   n_sims: Integer representing the number of desired simulated hands
    #   n_players: List of n in [2, 52] cards
    #   seed: Integer representing the desired seed. 1 by default
    # Output: A list of dictionaries, each dictionary representing a unique starting hand and having keys
    #   card_1: Rank of first card in hand
    #   card_2: Rank of second card in hand
    #   suited: A boolean - is the hand suited?
    #   wins: The number of wins that the hand achieved in B simulated hands. Fractional wins represent split pots
    #   total_hands: n_hands

    def unconditional_strength(self, n_sims, n_players, seed=1):
        r.seed(seed)
        starting_hands_strength = []
        n_starting_hands = len(self.starting_hands)
        for i in range(n_starting_hands):
            hand = self.starting_hands[i].copy()
            print('Now simulating hand ', hand, 'for ', n_players, ' players')
            my_hand = self.convert_hand_two_dicts(hand)
            wins = self.simulate_hands(my_hand, n_sims, n_players)
            hand.update({'wins': wins, 'total_hands': n_sims})
            starting_hands_strength.append(hand)
        return starting_hands_strength

    # This function determines the rankings of hands. It takes as input the output from unconitional_strength
    # and updates each dictionary item with the ranking of that hand.
    # Args:
    #   An output from unconditional_strength. List of dictionary objects.
    # Output: A list of dictionaries, each dictionary representing a unique starting hand and having keys
    #   card_1: Rank of first card in hand
    #   card_2: Rank of second card in hand
    #   suited: A boolean - is the hand suited?
    #   wins: The number of wins that the hand achieved in B simulated hands. Fractional wins represent split pots
    #   total_hands: n_hands
    #   ranking: an integer representing the ranking of the hand in the list, by wins. 1 is strongest, 169
    #            is weakest
    #   percentile: a number in [0,1] representing the share of the other 168 hands the given hand ranks better
    #               than

    def add_rankings(self, hands):
        # Get the number of wins from each hand
        n_wins = list(map(lambda c : -1*c['wins'], hands))
        orders = np.argsort(n_wins).tolist()
        for i in range(len(hands)):
            hand = hands[i]
            ranking = orders.index(i) + 1
            percentile = float(1 - ((ranking-1)/(len(hands)-1)))
            hand.update({'ranking': ranking, 'percentile': percentile})
        return hands

    # This function runs unconditional_strength and saves the results to the starting_hands folder.

    def run_simulation_and_save(self, n_sims):
        for i in range(2,10):
            hands = self.unconditional_strength(n_sims, i)
            hands_with_ranks = self.add_rankings(hands)
            name = 'starting_hands/' + 'u_' + str(i) + '_' + str(n_sims) + '.txt'
            with open(name, 'w') as f:
                json.dump(hands_with_ranks, f, indent=2)


if __name__ == '__main__':
    x = StartingHands()
    # x.run_simulation_and_save(10000)

    # Functions to troubleshoot.
    # test = x.unconditional_strength(1000,9)
    # print(*sorted(x.add_rankings(test), key=lambda c : -1*c['wins']), sep = '\n')





