from basic_items import card_items
from action import current_game
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

    # Sort cards and return them descending by value then ascending alphabetically by suit. For predictable returns
    # for testing later functions. Sort all the cards by default. This will also be used to sort kicker cards.
    def sort_some_cards(self, cards, n_cards=None):
        if not n_cards:
            n_cards = len(cards)
        return sorted(cards, key=lambda c : (-1*self.rank_values[c['rank']], c['suit']))[0:n_cards]

    def has_pair(self, cards):
        ranks = self.rank_object.copy()
        pair = []
        for card in cards:
            ranks[card['rank']] += 1
            if ranks[card['rank']] == 2:
                pair.extend([c for c in cards if c['rank'] == card['rank']])  # Add all cards but then get top 2 later
        if pair:
            return self.sort_some_cards(pair)[0:2]
        return False

    def has_two_pair(self, cards):
        ranks = self.rank_object.copy()
        n_pairs = 0
        two_pair = []
        for card in cards:
            ranks[card['rank']] += 1
            if ranks[card['rank']] == 2:
                n_pairs += 1
                two_pair.extend([c for c in cards if c['rank'] == card['rank']][0:2]) # Only get two cards in case there's more than 2
        if n_pairs >= 2:
            return self.sort_some_cards(two_pair)[0:4]
        return False

    def has_trips(self, cards):
        ranks = self.rank_object.copy()
        trips = []
        for card in cards:
            ranks[card['rank']] += 1
            if ranks[card['rank']] == 3:
                trips.extend([c for c in cards if c['rank'] == card['rank']][0:3]) # Only get three cards in case there's more than 3
        if trips:
            return self.sort_some_cards(trips)[0:3] # Only get the top 3
        else:
            return False

    def has_quads(self, cards):
        ranks = self.rank_object.copy()
        quads = []
        for card in cards:
            ranks[card['rank']] += 1
            if ranks[card['rank']] == 4:
                quads.extend([c for c in cards if c['rank'] == card['rank']][0:4]) # Only get four cards
                return self.sort_some_cards(quads)
        return False

    def has_straight(self, cards):
        # Sort the cards decending based on rank
        sorted_cards = sorted(cards, reverse=True, key=lambda c : self.rank_values[c['rank']])
        # Go through sorted_cards and vals_of_cards and delete one if there's more than one, so no duplicates
        ranks = self.rank_object.copy()
        sorted_cards_copy = sorted_cards.copy()

        for card in sorted_cards:
            ranks[card['rank']] += 1
            if ranks[card['rank']] == 2:
                sorted_cards_copy.remove(card)
                ranks[card['rank']] = 1

        sorted_cards = sorted_cards_copy
        # No straight if there's fewer than 5 distinct cards
        if len(sorted_cards) < 5:
            return False

        # Get the ranks of those sorted cards
        vals_of_cards = list(map(lambda c: self.rank_values[c['rank']], sorted_cards))
        # Sort separately according to wheel values
        sorted_cards_wheel = sorted(cards, reverse=True, key=lambda c: self.wheel_values[c['rank']])
        vals_of_cards_wheel = list(map(lambda c: self.wheel_values[c['rank']], sorted_cards_wheel))
        # See if a straight exists
        for i in range(len(sorted_cards) - 4):
            start = i
            end = i + 4
            these_cards = sorted_cards[start:(end + 1)] # five cards
            top_five_vals = vals_of_cards[start:(end + 1)]
            highest = max(top_five_vals)
            lowest = min(top_five_vals)
            if top_five_vals == list(range(highest, lowest - 1, -1)):
                return these_cards
            # Now check for wheel
            if i == len(sorted_cards) - 5:  # Last i
                top_five_vals = vals_of_cards_wheel[start:(end + 1)]
                if top_five_vals == [4, 3, 2, 1, 0]:
                    return sorted_cards_wheel[start:(end + 1)]
        return False

    def has_flush(self, cards):
        # Sort the cards decending based on rank
        if len(cards) < 5:
            return False
        sorted_cards = sorted(cards, reverse=True, key=lambda c: self.rank_values[c['rank']])
        suits = self.suit_object.copy()
        flush = []
        for card in sorted_cards:
            suits[card['suit']] += 1
            if suits[card['suit']] == 5:
                flush.extend([c for c in sorted_cards if c['suit'] == card['suit']][0:5]) # Already sorted so just take the top 5
                return flush
        return False

    def has_full_house(self, cards):
        if len(cards) < 5:
            return False
        # If there are trips...
        if trips := self.has_trips(cards):
            remaining_cards = [c for c in cards if c not in trips]
            # And a different pair...
            if pair := self.has_pair(remaining_cards):
                trips.extend(pair)
                return trips
        return False

    def has_straight_flush(self, cards):
        # Filter to same suit
        suits = self.suit_object.copy()
        same_suit = []
        for card in cards:
            suits[card['suit']] += 1
            if suits[card['suit']] == 5:
                same_suit = [c for c in cards if c['suit'] == card['suit']]
        # If there aren't 5 cards of the same suit, then no straight-flush
        if not same_suit:
            return False
        # Now just make a straight with the remaining cards of the same suit
        straight = self.has_straight(same_suit)
        if straight:
            return straight
        else:
            return False

    # Get the hex number of a sorted hand. Cards will be an output of one of the 'has' functions i.e. no more than 5 cards
    def hand_to_hex(self, cards):
        if type(cards) is dict:  # When giving just a single card
            rank = cards['rank']
            return hex(self.rank_values[rank])[2:]
        # Why does the below not work when cards is a single dictionary object?
        else:
            vals_of_cards = list(map(lambda c: self.rank_values[c['rank']], cards))
            hex_num = ''
            for v in vals_of_cards:
                hex_num += hex(v)[2:]
            return hex_num

    def get_hand_value(self, cards):
        starting = '0x00'  # Why does West have 2 zeroes in front? Just do it anyway for now
        if straight_flush := self.has_straight_flush(cards):
            return starting + '8' + self.hand_to_hex(straight_flush[0]) + '0000'  # For a straight flush, only need top card
        if quads := self.has_quads(cards):
            kicker = self.sort_some_cards([c for c in cards if c not in quads], n_cards=1)
            return starting + '7' + self.hand_to_hex(quads) + self.hand_to_hex(kicker)  # Need all cards for quads in case kicker is relevant
        if full_house := self.has_full_house(cards):
            return starting + '6' + self.hand_to_hex(full_house)
        if flush := self.has_flush(cards):
            return starting + '5' + self.hand_to_hex(flush)
        if straight := self.has_straight(cards):
            return starting + '4' + self.hand_to_hex(straight[0]) + '0000'  # Only highest card is relevant
        if trips := self.has_trips(cards):
            kickers = self.sort_some_cards([c for c in cards if c not in trips], n_cards=2)  # Trips returns 3 cards so need 2 kickers
            return starting + '3' + self.hand_to_hex(trips) + self.hand_to_hex(kickers)
        if twopair := self.has_two_pair(cards):
            kicker = self.sort_some_cards([c for c in cards if c not in twopair], n_cards=1)  # Need 1 kicker
            return starting + '2' + self.hand_to_hex(twopair) + self.hand_to_hex(kicker)
        if pair := self.has_pair(cards):
            kickers = self.sort_some_cards([c for c in cards if c not in pair], n_cards=3)  # Need 3 kickers
            return starting + '1' + self.hand_to_hex(pair) + self.hand_to_hex(kickers)
        return starting + '0' + self.hand_to_hex(self.sort_some_cards(cards, n_cards=5))  # High card

    def get_winning_hands(self, *hands):
        n_hands = len(hands)
        hand_values = []
        hand_hex_values = []
        for hand in hands:
            value = self.get_hand_value(hand)
            hand_hex_values.append(value)
            hand_values.append(int(value, 16))
        # Probably not the most efficient way to do this but oh well
        winner_index = [i for i in range(n_hands) if hand_values[i] == max(hand_values)]
        winning_hands = [hands[i] for i in range(n_hands) if i in winner_index]
        winning_hands_hex_vals = [hand_hex_values[i] for i in range(n_hands) if i in winner_index]
        return {'hands': winning_hands, 'hex': winning_hands_hex_vals}

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