import json
from basic_items import card_items
import guts
import starting_hand_strength
import importlib
importlib.reload(starting_hand_strength)

# First, make equity calculator. Things I need for equity calculator
#   A way to calculate pot odds

class Decision:
    hand_ops = guts.HandOperations()

    starting_hands = card_items['starting_hands']
    full_deck = card_items['full_deck_of_cards']

    # Hand strengths
    def __init__(self):
        self.u_2 = self.load_starting_hands(2)
        self.u_3 = self.load_starting_hands(3)
        self.u_4 = self.load_starting_hands(4)
        self.u_5 = self.load_starting_hands(5)
        self.u_6 = self.load_starting_hands(6)
        self.u_7 = self.load_starting_hands(7)
        self.u_8 = self.load_starting_hands(8)
        self.u_9 = self.load_starting_hands(9)

    def load_starting_hands(self, n_players):
        with open('starting_hands/u_' + str(n_players) + '_10000.txt', 'r') as f:
            data = json.load(f)
        return data

    # This function takes a 4 character string as an input and determines how good the hand is.
    # The string should be formatted '[card_1][card_2][suited/off][n_players]' where card_1 and card_2
    # are from 2 to a (ace), letters are lowercase. suited/off is either s or o. 10 is represented as t
    # Args:
    #   hand_string: length 4 string, such as 'q3s4' for Queen-3 suited with 4 players.
    # Output:
    #   A starting hand strength dictionary item, which has keys
    #   card_1: Rank of first card in hand
    #   card_2: Rank of second card in hand
    #   suited: A boolean - is the hand suited?
    #   wins: The number of wins that the hand achieved in B simulated hands. Fractional wins represent split pots
    #   total_hands: n_hands
    #   ranking: an integer representing the ranking of the hand in the list, by wins. 1 is strongest, 169
    #            is weakest
    #   percentile: a number in [0,1] representing the share of the other 168 hands the given hand ranks better
    #               than

    def how_good_is(self, hand_string):
        vals = self.hand_ops.rank_values
        inputs = ['2', '3', '4', '5', '6', '7', '8','9', 't', 'j', 'q', 'k', 'a']
        input_meanings = ['deuce', 'three', 'four', 'five', 'six', 'seven',
                          'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
        inputs_dict = {a: b for a, b in zip(inputs, input_meanings)}
        card_1 = inputs_dict[hand_string[0]]
        card_2 = inputs_dict[hand_string[1]]
        if vals[card_2] > vals[card_1]:
            card_2 = inputs_dict[hand_string[0]]
            card_1 = inputs_dict[hand_string[1]]
        suited = True if hand_string[2] == 's' else False
        n_players = hand_string[3]
        this_table = list(self.__dict__['u_' + str(n_players)])
        for i in this_table:
            if i['card_1'] == card_1 and i['card_2'] == card_2 and i['suited'] == suited:
                return i


    def calc_equity_postflop(self, action, current_game):
        pass




