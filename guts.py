from basic_items import card_items
from action import current_game
import random as r
import time as time

# What do I need?
# I need a function to take in two hands and the board and to tell me the equity of each hand.
# I need a function to take in any collection of cards and to find the best five card hand. It should see if there's a
# pair, triplet, straight, flush, etc, and to return the best hand.
# I'll use simulation to calculate equity
# Program starting ranges

# Just to save a bit of space
full_deck_of_cards = card_items['full_deck_of_cards']
rank_values = card_items['rank_values']
wheel_values = card_items['wheel_values']
rank_object = card_items['rank_object']
suit_object = card_items['suit_object']

# Example cards
some_cards = [{"rank": "ace", "suit": "clubs"},
              {"rank": "eight", "suit": "hearts"},
              {"rank": "queen", "suit": "diamonds"},
              {"rank": "three", "suit": "spades"},
              {"rank": "king", "suit": "hearts"}]

def best_hand(cards):
    pass

def is_pocket_pair(two_cards):
    if two_cards[0]['rank'] == two_cards[1]['rank']:
        return True
    else:
        return False

def is_suited(two_cards):
    if two_cards[0]['suit'] == two_cards[1]['suit']:
        return True
    else:
        return False

def get_street(table_cards):
    if len(table_cards) == 0:
        return 'pre-flop'
    elif len(table_cards) == 3:
        return 'flop'
    elif len(table_cards) == 4:
        return 'turn'
    elif len(table_cards) == 5:
        return 'river'
    return 'Error: Unknown street'

# Sort cards and return them descending by value then ascending alphabetically by suit. For predictable returns
# for testing later functions. Sort all the cards by default. This will also be used to sort kicker cards.
def sort_some_cards(some_cards, n_cards=None):
    if not n_cards:
        n_cards = len(some_cards)
    return sorted(some_cards, key=lambda c : (-1*rank_values[c['rank']], c['suit']))[0:n_cards]


assert (sort_some_cards([{"rank": "ace", "suit": "clubs"},
                         {"rank": "eight", "suit": "hearts"},
                         {"rank": "queen", "suit": "diamonds"},
                         {"rank": "eight", "suit": "spades"},
                         {"rank": "queen", "suit": "hearts"}]) == [{"rank": "ace", "suit": "clubs"},
                                                                   {"rank": "queen", "suit": "diamonds"},
                                                                   {"rank": "queen", "suit": "hearts"},
                                                                   {"rank": "eight", "suit": "hearts"},
                                                                   {"rank": "eight", "suit": "spades"}])

def has_pair(cards):
    ranks = rank_object.copy()
    pair = []
    for card in cards:
        ranks[card['rank']] += 1
        if ranks[card['rank']] == 2:
            pair.extend([c for c in cards if c['rank'] == card['rank']]) # Add all cards but then get top 2 later
    if pair:
        return sort_some_cards(pair)[0:2]
    return False


assert not has_pair([{"rank": "ace", "suit": "clubs"},
                     {"rank": "eight", "suit": "hearts"},
                     {"rank": "queen", "suit": "diamonds"},
                     {"rank": "three", "suit": "spades"},
                     {"rank": "king", "suit": "hearts"}])

assert has_pair([{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "eight", "suit": "spades"},
                 {"rank": "king", "suit": "hearts"}]) == [{"rank": "eight", "suit": "hearts"},
                                                          {"rank": "eight", "suit": "spades"}]

assert has_pair([{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "eight", "suit": "spades"},
                 {"rank": "ace", "suit": "hearts"}]) == [{"rank": "ace", "suit": "clubs"},
                                                         {"rank": "ace", "suit": "hearts"}]

assert has_pair([{"rank": "eight", "suit": "clubs"},
                {"rank": "eight", "suit": "hearts"},
                {"rank": "eight", "suit": "diamonds"}]) == [{"rank": "eight", "suit": "clubs"},
                                                            {"rank": "eight", "suit": "diamonds"}]
def has_two_pair(cards):
    ranks = rank_object.copy()
    n_pairs = 0
    two_pair = []
    for card in cards:
        ranks[card['rank']] += 1
        if ranks[card['rank']] == 2:
            n_pairs += 1
            two_pair.extend([c for c in cards if c['rank'] == card['rank']][0:2]) # Only get two cards in case there's more than 2
    if n_pairs >= 2:
        return sort_some_cards(two_pair)[0:4]
    return False


assert not has_two_pair([{"rank": "ace", "suit": "clubs"},
                      {"rank": "eight", "suit": "hearts"},
                      {"rank": "queen", "suit": "diamonds"},
                      {"rank": "eight", "suit": "spades"},
                      {"rank": "king", "suit": "hearts"}])

assert has_two_pair([{"rank": "ace", "suit": "clubs"},
                      {"rank": "eight", "suit": "hearts"},
                      {"rank": "queen", "suit": "diamonds"},
                      {"rank": "eight", "suit": "spades"},
                      {"rank": "queen", "suit": "hearts"}]) == [{"rank": "queen", "suit": "diamonds"},
                                                                {"rank": "queen", "suit": "hearts"},
                                                                {"rank": "eight", "suit": "hearts"},
                                                                {"rank": "eight", "suit": "spades"}]

# Tricky test - program needs to go all the way through cards for this reason.
assert has_two_pair([{"rank": "ace", "suit": "clubs"},
                      {"rank": "eight", "suit": "hearts"},
                      {"rank": "queen", "suit": "diamonds"},
                      {"rank": "eight", "suit": "spades"},
                      {"rank": "queen", "suit": "hearts"},
                      {"rank": "ace", "suit": "diamonds"}]) == [{"rank": "ace", "suit": "clubs"},
                                                                {"rank": "ace", "suit": "diamonds"},
                                                                {"rank": "queen", "suit": "diamonds"},
                                                                {"rank": "queen", "suit": "hearts"}]
def has_trips(cards):
    ranks = rank_object.copy()
    trips = []
    for card in cards:
        ranks[card['rank']] += 1
        if ranks[card['rank']] == 3:
            trips.extend([c for c in cards if c['rank'] == card['rank']][0:3]) # Only get three cards in case there's more than 3
    if trips:
        return sort_some_cards(trips)[0:3] # Only get the top 3
    else:
        return False


assert has_trips([{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]) == [{"rank": "queen", "suit": "diamonds"},
                                                            {"rank": "queen", "suit": "hearts"},
                                                            {"rank": "queen", "suit": "spades"}]

assert has_trips([{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]) == [{"rank": "queen", "suit": "diamonds"},
                                                            {"rank": "queen", "suit": "hearts"},
                                                            {"rank": "queen", "suit": "spades"}]


assert not has_trips([{"rank": "ace", "suit": "clubs"},
                      {"rank": "eight", "suit": "hearts"},
                      {"rank": "queen", "suit": "diamonds"},
                      {"rank": "eight", "suit": "spades"},
                      {"rank": "queen", "suit": "hearts"}])

def has_quads(cards):
    ranks = rank_object.copy()
    quads = []
    for card in cards:
        ranks[card['rank']] += 1
        if ranks[card['rank']] == 4:
            quads.extend([c for c in cards if c['rank'] == card['rank']][0:4]) # Only get four cards
            return sort_some_cards(quads)
    return False


assert has_quads([{"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]) == [{"rank": "queen", "suit": "clubs"},
                                                            {"rank": "queen", "suit": "diamonds"},
                                                            {"rank": "queen", "suit": "hearts"},
                                                            {"rank": "queen", "suit": "spades"}]

assert not has_quads([{"rank": "ace", "suit": "clubs"},
                      {"rank": "eight", "suit": "hearts"},
                      {"rank": "queen", "suit": "diamonds"},
                      {"rank": "eight", "suit": "spades"},
                      {"rank": "queen", "suit": "hearts"}])


def has_straight(cards):
    # Sort the cards decending based on rank
    sorted_cards = sorted(cards, reverse=True, key=lambda c : rank_values[c['rank']])
    # Go through sorted_cards and vals_of_cards and delete one if there's more than one, so no duplicates
    ranks = rank_object.copy()
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
    vals_of_cards = list(map(lambda c: rank_values[c['rank']], sorted_cards))
    # Sort separately according to wheel values
    sorted_cards_wheel = sorted(cards, reverse=True, key=lambda c: wheel_values[c['rank']])
    vals_of_cards_wheel = list(map(lambda c: wheel_values[c['rank']], sorted_cards_wheel))
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


assert has_straight([{'rank': 'ace', 'suit': 'clubs'},
                     {'rank': 'deuce', 'suit': 'hearts'},
                     {'rank': 'three', 'suit': 'diamonds'},
                     {'rank': 'four', 'suit': 'spades'},
                     {'rank': 'five', 'suit': 'hearts'},
                     {'rank': 'king', 'suit': 'diamonds'},
                     {'rank': 'six', 'suit': 'clubs'}]) == [{'rank': 'six', 'suit': 'clubs'},
                                                            {'rank': 'five', 'suit': 'hearts'},
                                                            {'rank': 'four', 'suit': 'spades'},
                                                            {'rank': 'three', 'suit': 'diamonds'},
                                                            {'rank': 'deuce', 'suit': 'hearts'}]

assert not has_straight([{'rank': 'ace', 'suit': 'clubs'},
                         {'rank': 'deuce', 'suit': 'hearts'},
                         {'rank': 'three', 'suit': 'diamonds'},
                         {'rank': 'jack', 'suit': 'spades'},
                         {'rank': 'five', 'suit': 'hearts'},
                         {'rank': 'king', 'suit': 'diamonds'},
                         {'rank': 'seven', 'suit': 'clubs'}])

assert not has_straight([{'rank': 'ace', 'suit': 'clubs'},
                         {'rank': 'three', 'suit': 'hearts'},
                         {'rank': 'three', 'suit': 'diamonds'},
                         {'rank': 'three', 'suit': 'spades'},
                         {'rank': 'five', 'suit': 'hearts'},
                         {'rank': 'king', 'suit': 'diamonds'},
                         {'rank': 'three', 'suit': 'clubs'}])

# Test for wheel
assert has_straight([{'rank': 'ace', 'suit': 'clubs'},
                     {'rank': 'deuce', 'suit': 'hearts'},
                     {'rank': 'three', 'suit': 'diamonds'},
                     {'rank': 'four', 'suit': 'spades'},
                     {'rank': 'five', 'suit': 'hearts'},
                     {'rank': 'king', 'suit': 'diamonds'},
                     {'rank': 'seven', 'suit': 'clubs'}]) == [{'rank': 'five', 'suit': 'hearts'},
                                                              {'rank': 'four', 'suit': 'spades'},
                                                              {'rank': 'three', 'suit': 'diamonds'},
                                                              {'rank': 'deuce', 'suit': 'hearts'},
                                                              {'rank': 'ace', 'suit': 'clubs'}]

def has_flush(cards):
    # Sort the cards decending based on rank
    if len(cards) < 5:
        return False
    sorted_cards = sorted(cards, reverse=True, key=lambda c: rank_values[c['rank']])
    suits = suit_object.copy()
    flush = []
    for card in sorted_cards:
        suits[card['suit']] += 1
        if suits[card['suit']] == 5:
            flush.extend([c for c in sorted_cards if c['suit'] == card['suit']][0:5]) # Already sorted so just take the top 5
            return flush
    return False


assert has_flush([{'rank': 'ace', 'suit': 'diamonds'},
                     {'rank': 'deuce', 'suit': 'hearts'},
                     {'rank': 'three', 'suit': 'diamonds'},
                     {'rank': 'four', 'suit': 'diamonds'},
                     {'rank': 'five', 'suit': 'hearts'},
                     {'rank': 'king', 'suit': 'diamonds'},
                     {'rank': 'seven', 'suit': 'diamonds'}]) == [{'rank': 'ace', 'suit': 'diamonds'},
                                                                 {'rank': 'king', 'suit': 'diamonds'},
                                                                 {'rank': 'seven', 'suit': 'diamonds'},
                                                                 {'rank': 'four', 'suit': 'diamonds'},
                                                                 {'rank': 'three', 'suit': 'diamonds'}]

assert has_flush([{'rank': 'ace', 'suit': 'diamonds'},
                     {'rank': 'deuce', 'suit': 'diamonds'},
                     {'rank': 'three', 'suit': 'diamonds'},
                     {'rank': 'four', 'suit': 'diamonds'},
                     {'rank': 'jack', 'suit': 'diamonds'},
                     {'rank': 'king', 'suit': 'diamonds'},
                     {'rank': 'seven', 'suit': 'diamonds'}]) == [{'rank': 'ace', 'suit': 'diamonds'},
                                                                 {'rank': 'king', 'suit': 'diamonds'},
                                                                 {'rank': 'jack', 'suit': 'diamonds'},
                                                                 {'rank': 'seven', 'suit': 'diamonds'},
                                                                 {'rank': 'four', 'suit': 'diamonds'}]


assert not has_flush([{'rank': 'ace', 'suit': 'clubs'},
                      {'rank': 'three', 'suit': 'hearts'},
                      {'rank': 'three', 'suit': 'diamonds'},
                      {'rank': 'three', 'suit': 'spades'},
                      {'rank': 'five', 'suit': 'hearts'},
                      {'rank': 'king', 'suit': 'diamonds'},
                      {'rank': 'three', 'suit': 'clubs'}])

def has_full_house(cards):
    if len(cards) < 5:
        return False
    # If there are trips...
    if trips := has_trips(cards):
        remaining_cards = [c for c in cards if c not in trips]
        # And a different pair...
        if pair := has_pair(remaining_cards):
            trips.extend(pair)
            return trips
    return False


assert has_full_house([{"rank": "eight", "suit": "clubs"},
                       {"rank": "eight", "suit": "hearts"},
                       {"rank": "eight", "suit": "diamonds"},
                       {"rank": "queen", "suit": "diamonds"},
                       {"rank": "queen", "suit": "spades"},
                       {"rank": "queen", "suit": "hearts"}]) == [{"rank": "queen", "suit": "diamonds"},
                                                                 {"rank": "queen", "suit": "hearts"},
                                                                 {"rank": "queen", "suit": "spades"},
                                                                 {"rank": "eight", "suit": "clubs"},
                                                                 {"rank": "eight", "suit": "diamonds"}]


def has_straight_flush(cards):
    # Filter to same suit
    suits = suit_object.copy()
    same_suit = []
    for card in cards:
        suits[card['suit']] += 1
        if suits[card['suit']] == 5:
            same_suit = [c for c in cards if c['suit'] == card['suit']]
    # If there aren't 5 cards of the same suit, then no straight-flush
    if not same_suit:
        return False
    # Now just make a straight with the remaining cards of the same suit
    straight = has_straight(same_suit)
    if straight:
        return straight
    else:
        return False


assert has_straight_flush([{'rank': 'queen', 'suit': 'diamonds'},
                           {'rank': 'nine', 'suit': 'diamonds'},
                           {'rank': 'three', 'suit': 'diamonds'},
                           {'rank': 'four', 'suit': 'diamonds'},
                           {'rank': 'jack', 'suit': 'diamonds'},
                           {'rank': 'king', 'suit': 'diamonds'},
                           {'rank': 'ten', 'suit': 'diamonds'}]) == [{'rank': 'king', 'suit': 'diamonds'},
                                                                     {'rank': 'queen', 'suit': 'diamonds'},
                                                                     {'rank': 'jack', 'suit': 'diamonds'},
                                                                     {'rank': 'ten', 'suit': 'diamonds'},
                                                                     {'rank': 'nine', 'suit': 'diamonds'}]
assert has_straight_flush([{'rank': 'queen', 'suit': 'diamonds'},
                           {'rank': 'nine', 'suit': 'diamonds'},
                           {'rank': 'three', 'suit': 'diamonds'},
                           {'rank': 'ace', 'suit': 'diamonds'},
                           {'rank': 'jack', 'suit': 'diamonds'},
                           {'rank': 'king', 'suit': 'diamonds'},
                           {'rank': 'ten', 'suit': 'diamonds'}]) == [{'rank': 'ace', 'suit': 'diamonds'},
                                                                     {'rank': 'king', 'suit': 'diamonds'},
                                                                     {'rank': 'queen', 'suit': 'diamonds'},
                                                                     {'rank': 'jack', 'suit': 'diamonds'},
                                                                     {'rank': 'ten', 'suit': 'diamonds'}]

assert has_straight_flush([{'rank': 'ace', 'suit': 'diamonds'},
                           {'rank': 'nine', 'suit': 'diamonds'},
                           {'rank': 'three', 'suit': 'diamonds'},
                           {'rank': 'four', 'suit': 'diamonds'},
                           {'rank': 'deuce', 'suit': 'diamonds'},
                           {'rank': 'king', 'suit': 'diamonds'},
                           {'rank': 'five', 'suit': 'diamonds'}]) == [{'rank': 'five', 'suit': 'diamonds'},
                                                                      {'rank': 'four', 'suit': 'diamonds'},
                                                                      {'rank': 'three', 'suit': 'diamonds'},
                                                                      {'rank': 'deuce', 'suit': 'diamonds'},
                                                                      {'rank': 'ace', 'suit': 'diamonds'}]
# Speed test

def speed_test(B):
    r.seed(1)
    start = time.time()
    royals, sflushes, quads, fhouses = 0, 0, 0, 0
    flushes, straights, trips, twopairs, pairs = 0, 0, 0, 0, 0
    for b in range(B):
        some_cards = r.sample(full_deck_of_cards, 7)
        if has_straight_flush(some_cards):
            sflushes += 1
            continue
        if has_quads(some_cards):
            quads += 1
            continue
        if has_full_house(some_cards):
            fhouses += 1
            continue
        if has_flush(some_cards):
            flushes += 1
            continue
        if has_straight(some_cards):
            straights += 1
            continue
        if has_trips(some_cards):
            trips += 1
            continue
        if has_two_pair(some_cards):
            twopairs += 1
            continue
        if has_pair(some_cards):
            pairs += 1
            continue
    end = time.time()
    print('Royals: ', royals/B)
    print('Straight-flushes: ', sflushes/B)
    print('Quads: ', quads/B)
    print('Full Houses: ', fhouses/B)
    print('Flushes: ', flushes/B)
    print('Straights: ', straights/B)
    print('Trips: ', trips/B)
    print('Two pairs: ', twopairs/B)
    print('Pairs: ', pairs/B)
    print(end - start)

speed_test(10000)

# Get the hex number of a sorted hand. Cards will be an output of one of the 'has' functions i.e. no more than 5 cards
def hand_to_hex(cards):
    if type(cards) is dict:  # When giving just a single card
        rank = cards['rank']
        return hex(rank_values[rank])[2:]
    # Why does the above line not work when cards is a single dictionary object?
    else:
        vals_of_cards = list(map(lambda c: rank_values[c['rank']], cards))
        hex_num = ''
        for v in vals_of_cards:
            hex_num += hex(v)[2:]
        return hex_num


assert hand_to_hex([{'rank': 'ace', 'suit': 'diamonds'},
                    {'rank': 'king', 'suit': 'diamonds'},
                    {'rank': 'queen', 'suit': 'diamonds'},
                    {'rank': 'jack', 'suit': 'diamonds'},
                    {'rank': 'ten', 'suit': 'diamonds'}]) == 'dcba9'

assert hand_to_hex({'rank': 'ten', 'suit': 'spades'}) == '9'

def get_hand_value(cards):
    starting = '0x00'  # Why does West have 2 zeroes in front? Just do it anyway for now
    if straight_flush := has_straight_flush(cards):
        return starting + '8' + hand_to_hex(straight_flush[0]) + '0000'  # For a straight flush, only need top card
    if quads := has_quads(cards):
        kicker = sort_some_cards([c for c in cards if c not in quads], n_cards=1)
        return starting + '7' + hand_to_hex(quads) + hand_to_hex(kicker)  # Need all cards for quads in case kicker is relevant
    if full_house := has_full_house(cards):
        return starting + '6' + hand_to_hex(full_house)
    if flush := has_flush(cards):
        return starting + '5' + hand_to_hex(flush)
    if straight := has_straight(cards):
        return starting + '4' + hand_to_hex(straight[0]) + '0000'  # Only highest card is relevant
    if trips := has_trips(cards):
        kickers = sort_some_cards([c for c in cards if c not in trips], n_cards=2)  # Trips returns 3 cards so need 2 kickers
        return starting + '3' + hand_to_hex(trips) + hand_to_hex(kickers)
    if twopair := has_two_pair(cards):
        kicker = sort_some_cards([c for c in cards if c not in twopair], n_cards=1)  # Need 1 kicker
        return starting + '2' + hand_to_hex(twopair) + hand_to_hex(kicker)
    if pair := has_pair(cards):
        kickers = sort_some_cards([c for c in cards if c not in pair], n_cards=3)  # Need 3 kickers
        return starting + '1' + hand_to_hex(pair) + hand_to_hex(kickers)
    return starting + '0' + hand_to_hex(sort_some_cards(cards, n_cards=5))  # High card


assert get_hand_value([{"rank": "deuce", "suit": "clubs"},
                       {"rank": "three", "suit": "clubs"},
                       {"rank": "ace", "suit": "clubs"},
                       {"rank": "queen", "suit": "clubs"},
                       {"rank": "queen", "suit": "diamonds"},
                       {"rank": "queen", "suit": "spades"},
                       {"rank": "queen", "suit": "hearts"}]) == '0x007bbbbd'



def get_winning_hands(*hands):
    n_hands = len(hands)
    hand_values = []
    hand_hex_values = []
    for hand in hands:
        value = get_hand_value(hand)
        hand_hex_values.append(value)
        hand_values.append(int(value, 16))
    # Probably not the most efficient way to do this but oh well
    winner_index = [i for i in range(n_hands) if hand_values[i] == max(hand_values)]
    winning_hands = [hands[i] for i in range(n_hands) if i in winner_index]
    winning_hands_hex_vals = [hand_hex_values[i] for i in range(n_hands) if i in winner_index]
    return {'hands': winning_hands, 'hex': winning_hands_hex_vals}

def look_at_some_hands():
    while True:
        cards1 = r.sample(full_deck_of_cards, 7); print('Hand 1', *cards1, sep='\n')
        cards2 = r.sample(full_deck_of_cards, 7); print('Hand 2', *cards2, sep='\n')
        cards3 = r.sample(full_deck_of_cards, 7); print('Hand 3', *cards3, sep='\n')
        win = get_winning_hands(cards1,cards2,cards3)
        print('winner:', *win['hands'], win['hex'], sep='\n')
        contin = input('Continue? N to stop')
        if contin == 'N':
            break

my_hand = current_game['yourCards']
n_players = len(current_game['players'])
street = get_street(current_game['tableCards'])