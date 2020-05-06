import unittest
from guts import HandOperations

class HandOperationsTest(unittest.TestCase):

    def setUp(self):
        self.hand_ops = HandOperations()

    def test_sort_some_cards(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "eight", "suit": "spades"},
                 {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "hearts"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "spades"}]

        self.assertEqual(self.hand_ops.sort_some_cards(cards), answer)

    def test_has_pair_no_pair(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "three", "suit": "spades"},
                 {"rank": "king", "suit": "hearts"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)

        self.assertFalse(self.hand_ops.has_pair(sorted_cards))

    def test_has_pair_one_pair(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "eight", "suit": "spades"},
                 {"rank": "king", "suit": "hearts"}]

        answer = [{"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "spades"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_pair(sorted_cards), answer)

    def test_has_pair_two_pairs(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "ace", "suit": "hearts"}]

        answer = [{"rank": "ace", "suit": "clubs"},
                   {"rank": "ace", "suit": "hearts"}]

        sorted_input = self.hand_ops.sort_some_cards(cards)

        self.assertEqual(self.hand_ops.has_pair(sorted_input), answer)

    def test_has_pair_trips(self):

        cards = [{"rank": "eight", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "eight", "suit": "diamonds"}]

        answer = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "diamonds"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)

        self.assertEqual(self.hand_ops.has_pair(sorted_cards), answer)

    def test_has_two_pair_not(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "king", "suit": "hearts"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertFalse(self.hand_ops.has_two_pair(sorted_cards))

    def test_has_two_pair(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "eight", "suit": "hearts"},
                   {"rank": "eight", "suit": "spades"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_two_pair(sorted_cards), answer)

    def test_has_two_pair_long(self):
        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"},
                  {"rank": "ace", "suit": "diamonds"}]

        answer = [{"rank": "ace", "suit": "clubs"},
                   {"rank": "ace", "suit": "diamonds"},
                   {"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_two_pair(sorted_cards), answer)

    def test_has_trips_not(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertFalse(self.hand_ops.has_trips(sorted_cards))

    def test_has_trips_trips(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_trips(sorted_cards), answer)

    def has_trips_two_trips(self):

        cards = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_trips(sorted_cards), answer)

    def test_has_quads_not(self):

        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertFalse(self.hand_ops.has_quads(sorted_cards))

    def test_has_quads(self):
        cards = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "queen", "suit": "clubs"},
                   {"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_quads(sorted_cards), answer)

    def test_has_straight_false_1(self):

        cards = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'three', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'clubs'}]

        self.assertFalse(self.hand_ops.has_straight(cards))

    def test_has_straight_false_2(self):

        cards = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'clubs'}]

        self.assertFalse(self.hand_ops.has_straight(cards), False)

    def test_has_straight(self):

        cards = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'six', 'suit': 'clubs'}]

        answer = [{'rank': 'six', 'suit': 'clubs'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'hearts'}]

        self.assertEqual(self.hand_ops.has_straight(cards), answer)

    def test_has_straight_wheel(self):

        cards = [{'rank': 'ace', 'suit': 'clubs'},
                  {'rank': 'deuce', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'spades'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'clubs'}]

        answer = [{'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'ace', 'suit': 'clubs'}]

        self.assertEqual(self.hand_ops.has_straight(cards), answer)

    def test_has_straight_five_cards(self):
        cards = [{'rank': 'king', 'suit': 'diamonds'},
                 {'rank': 'queen', 'suit': 'diamonds'},
                 {'rank': 'jack', 'suit': 'diamonds'},
                 {'rank': 'ten', 'suit': 'diamonds'},
                 {'rank': 'nine', 'suit': 'diamonds'}]
        self.assertEqual(self.hand_ops.has_straight(cards), cards)


    def test_has_flush_not(self):

        cards = [{'rank': 'ace', 'suit': 'clubs'},
                  {'rank': 'three', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'spades'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'clubs'}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertFalse(self.hand_ops.has_flush(sorted_cards))

    def test_has_flush_same_suit(self):

        cards = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'diamonds'}]

        answer = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_flush(sorted_cards), answer)

    def test_has_flush_more_than_1_suit(self):

        cards = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'diamonds'}]

        answer = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'diamonds'}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_flush(sorted_cards), answer)

    def test_has_full_house(self):

        cards = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"},
                   {"rank": "eight", "suit": "clubs"},
                   {"rank": "eight", "suit": "diamonds"}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_full_house(sorted_cards), answer)

    def test_has_straight_flush(self):

        cards = [{'rank': 'queen', 'suit': 'diamonds'},
                  {'rank': 'nine', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'ten', 'suit': 'diamonds'}]

        answer = [{'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'queen', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'ten', 'suit': 'diamonds'},
                   {'rank': 'nine', 'suit': 'diamonds'}]
        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_straight_flush(sorted_cards), answer)

    def test_has_straight_flush_royal(self):
        cards = [{'rank': 'queen', 'suit': 'diamonds'},
                  {'rank': 'ace', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'ten', 'suit': 'diamonds'}]

        answer = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'queen', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'ten', 'suit': 'diamonds'}]
        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_straight_flush(sorted_cards), answer)

    def test_has_straight_flush_wheel(self):
        cards = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'nine', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'five', 'suit': 'diamonds'}]

        answer = [{'rank': 'five', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'diamonds'},
                   {'rank': 'ace', 'suit': 'diamonds'}]

        sorted_cards = self.hand_ops.sort_some_cards(cards)
        self.assertEqual(self.hand_ops.has_straight_flush(sorted_cards), answer)

    def test_hand_to_hex(self):
        input1 = [{'rank': 'ace', 'suit': 'diamonds'},
                    {'rank': 'king', 'suit': 'diamonds'},
                    {'rank': 'queen', 'suit': 'diamonds'},
                    {'rank': 'jack', 'suit': 'diamonds'},
                    {'rank': 'ten', 'suit': 'diamonds'}]
        input2 = {'rank': 'ten', 'suit': 'spades'}

        self.assertEqual(self.hand_ops.hand_to_hex(input1), 'dcba9')
        self.assertEqual(self.hand_ops.hand_to_hex(input2), '9')

    def test_get_hand_value(self):

        input1 = [{"rank": "deuce", "suit": "clubs"},
                  {"rank": "three", "suit": "clubs"},
                  {"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        self.assertEqual(self.hand_ops.get_hand_value(input1), '0x007bbbbd')

    def test_get_winning_hands_full_ring(self):

        table_cards = [{'rank': 'ace', 'suit': 'spades'},
                       {'rank': 'seven', 'suit': 'diamonds'},
                       {'rank': 'queen', 'suit': 'clubs'},
                       {'rank': 'nine', 'suit': 'clubs'},
                       {'rank': 'queen', 'suit': 'spades'}]

        my_hand = self.hand_ops.sort_some_cards([{'rank': 'ace', 'suit': 'hearts'},
                                                 {'rank': 'ace', 'suit': 'diamonds'}])

        hand_2 = self.hand_ops.sort_some_cards([{'rank': 'nine', 'suit': 'spades'},
                                                {'rank': 'queen', 'suit': 'hearts'}])

        hand_3 = self.hand_ops.sort_some_cards([{'rank': 'five', 'suit': 'spades'},
                                                {'rank': 'five', 'suit': 'clubs'}])

        hand_4 = self.hand_ops.sort_some_cards([{'rank': 'ten', 'suit': 'spades'},
                                                {'rank': 'ten', 'suit': 'hearts'}])

        hand_5 = self.hand_ops.sort_some_cards([{'rank': 'eight', 'suit': 'hearts'},
                                                {'rank': 'jack', 'suit': 'hearts'}])

        hand_6 = self.hand_ops.sort_some_cards([{'rank': 'king', 'suit': 'diamonds'},
                                                {'rank': 'four', 'suit': 'hearts'}])

        hand_7 = self.hand_ops.sort_some_cards([{'rank': 'four', 'suit': 'clubs'},
                                                {'rank': 'eight', 'suit': 'spades'}])

        hand_8 = self.hand_ops.sort_some_cards([{'rank': 'six', 'suit': 'diamonds'},
                                                {'rank': 'deuce', 'suit': 'spades'}])

        hand_9 = self.hand_ops.sort_some_cards([{'rank': 'nine', 'suit': 'hearts'},
                                                {'rank': 'three', 'suit': 'diamonds'}])


        winning_hands = self.hand_ops.get_winning_hands([my_hand, hand_2, hand_3,hand_4,hand_5,
                                                         hand_6,hand_7,hand_8,hand_9], table_cards)

        self.assertEqual(winning_hands['winners'], [my_hand])
        self.assertEqual(winning_hands['hex'], '0x006dddbb')

if __name__=='__main__':
      unittest.main()
