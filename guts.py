from basic_items import card_items
import random as r

# What do I need?
# I need a function to take in two hands and the board and to tell me the equity of each hand.
# I need a function to take in any collection of cards and to find the best five card hand. It should see if there's a
# pair, triplet, straight, flush, etc, and to return the best hand.
# I'll use simulation to calculate equity
# Program starting ranges

class HandOperations:

    full_deck_of_cards = card_items['full_deck_of_cards']
    rank_values = card_items['rank_values']
    wheel_values = card_items['wheel_values']
    rank_object = card_items['rank_object']
    suit_object = card_items['suit_object']

    # This function sorts a list of cards descending by rank, then ascending alphabetically by suit
    # Args:
    #   cards: List of cards of length n > 1
    # Output: List of sorted cards of length n

    # Note that in all later functions which require sorted cards as inputs, the sort is to be done using
    # the "sort_some_cards" function. Also note that if value_set is set to wheel_values, then the function
    # will sort as if aces are the lowest value rank.

    def sort_some_cards(self, cards, value_set=rank_values):
        return sorted(cards, key=lambda c : (-1*value_set[c['rank']], c['suit']))

    # This function determines if a hand has a pair, and returns the highest pair if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [2,7]
    # Output: List of sorted cards of length 2 or False

    def has_pair(self, sorted_cards):
        if len(sorted_cards) < 2:
            return False
        ranks = {}
        for card in sorted_cards:
            rank_of_card = card['rank']
            if ranks.get(rank_of_card):
                ranks[rank_of_card] += 1
                if ranks[rank_of_card] == 2:
                    return [c for c in sorted_cards if c['rank'] == rank_of_card][0:2]
            else:
                ranks[rank_of_card] = 1
        return False

    # This function determines if a hand has a two-pair, and returns the highest two-pair if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [4,7]
    # Output: List of sorted cards of length 4 or False

    def has_two_pair(self, sorted_cards):
        if len(sorted_cards) < 4:
            return False
        if first_pair := self.has_pair(sorted_cards):
            sorted_cards_less_rank_of_pair = [c for c in sorted_cards if c['rank'] != first_pair[0]['rank']]
            if second_pair := self.has_pair(sorted_cards_less_rank_of_pair):
                return [*first_pair, *second_pair]
        return False

    # This function determines if a hand has trips, and returns the highest trips if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [3,7]
    # Output: List of sorted cards of length 3 or False

    def has_trips(self, sorted_cards):
        if len(sorted_cards) < 3:
            return False
        ranks = {}
        for card in sorted_cards:
            rank_of_card = card['rank']
            if ranks.get(rank_of_card):
                ranks[rank_of_card] += 1
                if ranks.get(rank_of_card) == 3:
                    return [c for c in sorted_cards if c['rank'] == rank_of_card][0:3]
            else:
                ranks[rank_of_card] = 1
        return False

    # This function determines if a hand has quads, and returns the quads if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [4,7]
    # Output: List of sorted cards of length 4 or False

    def has_quads(self, sorted_cards):
        if len(sorted_cards) < 4:
            return False
        ranks = {}
        for card in sorted_cards:
            rank_of_card = card['rank']
            if ranks.get(rank_of_card):
                ranks[rank_of_card] += 1
                if ranks.get(rank_of_card) == 4:
                    return [c for c in sorted_cards if c['rank'] == rank_of_card][0:4]
            else:
                ranks[rank_of_card] = 1
        return False

    # This function determines if a hand has a straight and returns it if so. If not, returns false.
    # Args:
    #   sorted_cards: List of cards of length n in [5,7] (need not be sorted)
    # Output: List of sorted cards of length 5 or False

    def has_straight(self, cards):

        # Helper function which actually finds the straight. Will run this on the hand using 1) regular "rank_values",
        # and then 2) "wheel_values" to check for a wheel

        def find_straight(some_cards, value_set):
            sorted_cards = self.sort_some_cards(some_cards, value_set=value_set)
            if len(sorted_cards) < 5:
                return False
            straight = [sorted_cards[0]]
            # Rank and value of first card in hand
            rank_of_card = sorted_cards[0]['rank']
            rank_of_card_value = self.rank_values[rank_of_card]
            num_cards_in_row = 1
            for i in range(1, len(sorted_cards)):


                # First, is it even mathematically possible to get a straight (are there enough cards remaining)?
                n_cards_left = len(sorted_cards) - i
                n_cards_needed = 5 - num_cards_in_row
                if n_cards_needed > n_cards_left:
                    return False

                card = sorted_cards[i]
                current_rank = card['rank']
                current_value = value_set[current_rank]

                if current_rank == rank_of_card:  # Duplicate rank. Skip these
                    continue

                if current_value == rank_of_card_value - 1: # Two cards are in sequence
                    num_cards_in_row += 1
                    straight.append(card)
                    if num_cards_in_row == 5:
                        return straight
                else:
                    num_cards_in_row = 1
                    straight = [card]
                rank_of_card = card['rank']
                rank_of_card_value = self.rank_values[rank_of_card]

        # Find non-wheel straight
        high_straight = find_straight(cards, value_set=self.rank_values)
        if high_straight:
            return high_straight
        wheel_straight = find_straight(cards, value_set=self.wheel_values)
        if wheel_straight:
            return wheel_straight
        return False

    # This function determines if a hand has a flush and returns it if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [5,7]
    # Output: List of sorted cards of length 5 or False

    def has_flush(self, sorted_cards):
        # Sort the cards decending based on rank
        if len(sorted_cards) < 5:
            return False

        suits = {}
        flush = []
        for card in sorted_cards:
            this_card_suit = card['suit']
            flush.append(card)
            if suits.get(this_card_suit):
                suits[this_card_suit] += 1
                if suits[this_card_suit] == 5:
                    # Return only the cards that have the same suit as the current card. There will be 5 of them
                    return [c for c in flush if c['suit'] == this_card_suit]
            else:
                suits[this_card_suit] = 1
        return False

    # This function determines if a hand has a full house and returns it if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [5,7]
    # Output: List of sorted cards of length 5 or False

    def has_full_house(self, sorted_cards):
        if len(sorted_cards) < 5:
            return False
        # If there are trips...
        if trips := self.has_trips(sorted_cards):
            remaining_cards = [c for c in sorted_cards if c not in trips]
            # And a different pair...
            if pair := self.has_pair(remaining_cards):
                return [*trips, *pair]
        return False

    # This function determines if a hand has a straight flush and returns it if so. If not, returns false.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [5,7]
    # Output: List of sorted cards of length 5 or False

    def has_straight_flush(self, sorted_cards):
        # Find flush and get all cards of same suit as flush
        if flush := self.has_flush(sorted_cards):
            same_suit_cards = [c for c in sorted_cards if c['suit'] == flush[0]['suit']]
            # Now just make a straight with the remaining cards of the same suit
            if straight := self.has_straight(same_suit_cards):
                return straight
        return False

    # This function calculates the hex value of some cards based on rank. It does not consider made hands.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [1,5], or 1 card
    # Output: String of length n representing the hex value of the cards

    def hand_to_hex(self, sorted_cards):
        assert len(sorted_cards) in range(1,6)
        if type(sorted_cards) is dict:  # When given just a single card (just a dict object)
            rank = sorted_cards['rank']
            return hex(self.rank_values[rank])[2:]
        # Why does the below not work when cards is a single dictionary object?
        else:
            vals_of_cards = list(map(lambda c: self.rank_values[c['rank']], sorted_cards))
            hex_num = ''
            for v in vals_of_cards:
                hex_num += hex(v)[2:]
            return hex_num

    # This function calculates the hex value of some cards by calculating the made hand plus kicker cards.
    # Args:
    #   sorted_cards: List of sorted cards of length n in [5,7]
    # Output: String length 10 representing the hex value of the best 5-card hand of sorted_cards

    def get_hand_value(self, sorted_cards):
        starting = '0x00'  # Why does West have 2 zeroes in front? Just do it anyway for now
        if straight_flush := self.has_straight_flush(sorted_cards):
            return starting + '8' + self.hand_to_hex(straight_flush[0]) + '0000'  # For a straight flush, only need top card
        if quads := self.has_quads(sorted_cards):
            kicker = self.sort_some_cards([c for c in sorted_cards if c not in quads])[0]
            return starting + '7' + self.hand_to_hex(quads) + self.hand_to_hex(kicker)  # Need all cards for quads in case kicker is relevant
        if full_house := self.has_full_house(sorted_cards):
            return starting + '6' + self.hand_to_hex(full_house)
        if flush := self.has_flush(sorted_cards):
            return starting + '5' + self.hand_to_hex(flush)
        if straight := self.has_straight(sorted_cards):
            return starting + '4' + self.hand_to_hex(straight[0]) + '0000'  # Only highest card is relevant
        if trips := self.has_trips(sorted_cards):
            kickers = self.sort_some_cards([c for c in sorted_cards if c not in trips])[0:2]  # Trips returns 3 cards so need 2 kickers
            return starting + '3' + self.hand_to_hex(trips) + self.hand_to_hex(kickers)
        if twopair := self.has_two_pair(sorted_cards):
            kicker = self.sort_some_cards([c for c in sorted_cards if c not in twopair])[0]  # Need 1 kicker
            return starting + '2' + self.hand_to_hex(twopair) + self.hand_to_hex(kicker)
        if pair := self.has_pair(sorted_cards):
            kickers = self.sort_some_cards([c for c in sorted_cards if c not in pair])[0:3]  # Need 3 kickers
            return starting + '1' + self.hand_to_hex(pair) + self.hand_to_hex(kickers)
        return starting + '0' + self.hand_to_hex(self.sort_some_cards(sorted_cards)[0:5])  # High card

    # This function takes a number of 2-card hands and the table cards and determines the winning hands
    # Args:
    #   list_of_hands: List length N of N hands. Each hand is a list of n=2 cards. Need not be sorted
    #   table_cards: List length n in [3.5]. Need not be sorted
    # Output: An object containing
    #   winners: List of winning 2-card hands. Note that each hand is itself a list of cards, so winners is a list
    #          of list of cards
    #   hex: The hex value of the winning hand(s). String of length 10

    def get_winning_hands(self, list_of_hands, table_cards):

        n_hands = len(list_of_hands)
        hand_values = []
        hand_hex_values = []
        for hand in list_of_hands:
            hand_with_table_cards = self.sort_some_cards([*hand, *table_cards])
            value = self.get_hand_value(hand_with_table_cards)
            hand_hex_values.append(value)
            hand_values.append(int(value, 16))
        # Is there a better way to do this?

        # Which hands are the winners, by index
        winner_index = [i for i in range(n_hands) if hand_values[i] == max(hand_values)]
        # These are the winnings hand(s)
        winning_hands = [list_of_hands[i] for i in winner_index]
        # This is the hex of the winning hands. Multiple winning hands (split pot) must have same value. So
        # there will always be just 1 hex value returned.
        return {'winners': winning_hands, 'hex': hand_hex_values[winner_index[0]]}

    def look_at_some_hands(self):
        while True:
            cards1 = r.sample(self.full_deck_of_cards, 7); print('Hand 1', *cards1, sep='\n')
            cards2 = r.sample(self.full_deck_of_cards, 7); print('Hand 2', *cards2, sep='\n')
            cards3 = r.sample(self.full_deck_of_cards, 7); print('Hand 3', *cards3, sep='\n')
            win = self.get_winning_hands(cards1,cards2,cards3)
            print('winner:', *win['hands'], win['hex'], sep='\n')
            contin = input('Continue? N to stop')
            if contin == 'N':
                break

    def is_pocket_pair(self, two_cards):
        if two_cards[0]['rank'] == two_cards[1]['rank']:
            return True
        else:
            return False

    def is_suited(self, two_cards):
        if two_cards[0]['suit'] == two_cards[1]['suit']:
            return True
        else:
            return False

    def get_street(self, table_cards):
        if len(table_cards) == 0:
            return 'pre-flop'
        elif len(table_cards) == 3:
            return 'flop'
        elif len(table_cards) == 4:
            return 'turn'
        elif len(table_cards) == 5:
            return 'river'
        return 'Error: Unknown street'

    # Returns the size of the pot and the current largest bet. Note that because player 'pot'
    # shows merely how much money the player has in front of them, current largest
    # bet shouldn't be interpreted in isolation.

    def size_of_pot_and_current_largest_bet(self, game):
        largest_bet = 0
        pot = 0
        for p in game['players']:
            player_pot = p['pot']
            pot += player_pot
            if player_pot > largest_bet:
                largest_bet = player_pot
        return pot

    # Returns the amount of money that player_username is required to call

    def my_current_bet(self, player_username, current_game, max_bet):
        for p in current_game['players']:
            if p['username'] == player_username:
                return max_bet - p['pot']



