from basic_items import card_items
import guts
import importlib
importlib.reload(guts)
import random as r
import json
import os

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
            full_deck_of_cards = self.full_deck
            card_1 = hand['card_1']
            card_2 = hand['card_2']

            # Declare the actual 2 cards that consist the hand
            if hand['suited']:
                # The particular suits don't matter because of symmetry
                my_hand = [{'rank': card_1, 'suit': 'hearts'},
                           {'rank': card_2, 'suit': 'hearts'}]
            else:
                my_hand = [{'rank': card_1, 'suit': 'hearts'},
                           {'rank': card_2, 'suit': 'diamonds'}]

            full_deck_minus_my_hand = [i for i in full_deck_of_cards if i not in my_hand]
            rest_of_cards = full_deck_minus_my_hand
            assert len(rest_of_cards) == 50
            wins = 0
            for b in range(n_sims):
                if b % 1000 == 0 and b > 0:
                    print('Sim number ', b)
                all_hands = [my_hand]  # This list of lists of dicts will hold all hands of the players at the table
                # Now deal the rest of the hands at the table, and add each hand to all_hands
                for j in range(n_players-1):
                    opponent_hand, rest_of_cards = self.deal_cards(2, rest_of_cards)
                    all_hands.append(opponent_hand)
                    assert len(rest_of_cards) == (50 - 2*(j+1))
                # Deal 5 table cards
                table_cards, rest_of_cards = self.deal_cards(5, rest_of_cards)
                assert len(rest_of_cards) == 52 - 2*n_players - 5
                # Find the winning hands
                winners = self.hand_ops.get_winning_hands(all_hands, table_cards)
                winning_hands = winners['winners']
                if my_hand in winning_hands:
                    wins += 1/len(winning_hands)  # Splits are shared equally
                # Reset rest_of_cards
                rest_of_cards = full_deck_minus_my_hand
            hand.update({'wins': wins, 'total_hands': n_sims})
            starting_hands_strength.append(hand)
        return starting_hands_strength


    def run_simulation_and_save(self, n_sims):
        for i in range(2,10):
            hands = self.unconditional_strength(n_sims, i)
            name = 'starting_hands/' + 'u_' + str(i) + '_' + str(n_sims) + '.txt'
            with open(name, 'w') as f:
                json.dump(hands, f, indent=2)


# x = StartingHands()
# x.run_simulation_and_save(100)





