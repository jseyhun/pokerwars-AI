
# Basic items that will be called upon many times

full_deck_of_cards = [
    {'rank': 'ace', 'suit': 'spades'},
    {'rank': 'deuce', 'suit': 'spades'},
    {'rank': 'three', 'suit': 'spades'},
    {'rank': 'four', 'suit': 'spades'},
    {'rank': 'five', 'suit': 'spades'},
    {'rank': 'six', 'suit': 'spades'},
    {'rank': 'seven', 'suit': 'spades'},
    {'rank': 'eight', 'suit': 'spades'},
    {'rank': 'nine', 'suit': 'spades'},
    {'rank': 'ten', 'suit': 'spades'},
    {'rank': 'jack', 'suit': 'spades'},
    {'rank': 'queen', 'suit': 'spades'},
    {'rank': 'king', 'suit': 'spades'},
    {'rank': 'ace', 'suit': 'clubs'},
    {'rank': 'deuce', 'suit': 'clubs'},
    {'rank': 'three', 'suit': 'clubs'},
    {'rank': 'four', 'suit': 'clubs'},
    {'rank': 'five', 'suit': 'clubs'},
    {'rank': 'six', 'suit': 'clubs'},
    {'rank': 'seven', 'suit': 'clubs'},
    {'rank': 'eight', 'suit': 'clubs'},
    {'rank': 'nine', 'suit': 'clubs'},
    {'rank': 'ten', 'suit': 'clubs'},
    {'rank': 'jack', 'suit': 'clubs'},
    {'rank': 'queen', 'suit': 'clubs'},
    {'rank': 'king', 'suit': 'clubs'},
    {'rank': 'ace', 'suit': 'hearts'},
    {'rank': 'deuce', 'suit': 'hearts'},
    {'rank': 'three', 'suit': 'hearts'},
    {'rank': 'four', 'suit': 'hearts'},
    {'rank': 'five', 'suit': 'hearts'},
    {'rank': 'six', 'suit': 'hearts'},
    {'rank': 'seven', 'suit': 'hearts'},
    {'rank': 'eight', 'suit': 'hearts'},
    {'rank': 'nine', 'suit': 'hearts'},
    {'rank': 'ten', 'suit': 'hearts'},
    {'rank': 'jack', 'suit': 'hearts'},
    {'rank': 'queen', 'suit': 'hearts'},
    {'rank': 'king', 'suit': 'hearts'},
    {'rank': 'ace', 'suit': 'diamonds'},
    {'rank': 'deuce', 'suit': 'diamonds'},
    {'rank': 'three', 'suit': 'diamonds'},
    {'rank': 'four', 'suit': 'diamonds'},
    {'rank': 'five', 'suit': 'diamonds'},
    {'rank': 'six', 'suit': 'diamonds'},
    {'rank': 'seven', 'suit': 'diamonds'},
    {'rank': 'eight', 'suit': 'diamonds'},
    {'rank': 'nine', 'suit': 'diamonds'},
    {'rank': 'ten', 'suit': 'diamonds'},
    {'rank': 'jack', 'suit': 'diamonds'},
    {'rank': 'queen', 'suit': 'diamonds'},
    {'rank': 'king', 'suit': 'diamonds'},
]

# Order of card values

rank_values = {'ace': 13,
               'deuce': 1,
               'three': 2,
               'four': 3,
               'five': 4,
               'six': 5,
               'seven': 6,
               'eight': 7,
               'nine': 8,
               'ten': 9,
               'jack': 10,
               'queen': 11,
               'king': 12}

# Values are different for a wheel (Ace to 5 straight)

wheel_values = {'ace': 0,
                'deuce': 1,
                'three': 2,
                'four': 3,
                'five': 4,
                'six': 5,
                'seven': 6,
                'eight': 7,
                'nine': 8,
                'ten': 9,
                'jack': 10,
                'queen': 11,
                'king': 12}

# These will be created by the functions which determine if a hand has a pair, three of a kind, and so on
# They'll be called many times so I'll just create them here

rank_object = {'ace': 0,
               'deuce': 0,
               'three': 0,
               'four': 0,
               'five': 0,
               'six': 0,
               'seven': 0,
               'eight': 0,
               'nine': 0,
               'ten': 0,
               'jack': 0,
               'queen': 0,
               'king': 0}

suit_object = {'spades': 0,
               'diamonds': 0,
               'clubs': 0,
               'hearts': 0}

# Create all starting hands
def create_starting_hands():
    # First, find all 2 card combinations
    hands = []
    ranks = sorted(list(rank_object.keys()), key = lambda c : -1*rank_values[c])
    for i in ranks:
        for j in ranks:
            i_value = rank_values[i]
            j_value = rank_values[j]
            if i_value >= j_value:
                if i_value != j_value:
                    hands.append({'card_1': i, 'card_2': j, 'suited': True})
                hands.append({'card_1': i, 'card_2': j, 'suited': False})
    return hands

starting_hands = create_starting_hands()

card_items = {'full_deck_of_cards':full_deck_of_cards,
              'rank_values': rank_values,
              'wheel_values': wheel_values,
              'rank_object': rank_object,
              'suit_object': suit_object,
              'starting_hands': starting_hands}