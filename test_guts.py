import unittest
from guts import HandOperations

class HandOperationsTest(unittest.TestCase):

    def setUp(self):
        self.hand_ops = HandOperations()

    def test_sort_some_cards(self):

        input = [{"rank": "ace", "suit": "clubs"},
                 {"rank": "eight", "suit": "hearts"},
                 {"rank": "queen", "suit": "diamonds"},
                 {"rank": "eight", "suit": "spades"},
                 {"rank": "queen", "suit": "hearts"}]

        answer = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "hearts"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "spades"}]

        self.assertEqual(self.hand_ops.sort_some_cards(input), answer)

    def test_has_pair(self):

        input1 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "three", "suit": "spades"},
                  {"rank": "king", "suit": "hearts"}]

        input2 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "king", "suit": "hearts"}]

        answer2 = [{"rank": "eight", "suit": "hearts"},
                   {"rank": "eight", "suit": "spades"}]

        input3 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "ace", "suit": "hearts"}]

        answer3 = [{"rank": "ace", "suit": "clubs"},
                   {"rank": "ace", "suit": "hearts"}]

        input4 = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"}]

        answer4 = [{"rank": "eight", "suit": "clubs"},
                   {"rank": "eight", "suit": "diamonds"}]

        self.assertEqual(self.hand_ops.has_pair(input1), False)
        self.assertEqual(self.hand_ops.has_pair(input2), answer2)
        self.assertEqual(self.hand_ops.has_pair(input3), answer3)
        self.assertEqual(self.hand_ops.has_pair(input4), answer4)

    def test_has_two_pair(self):

        input1 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "king", "suit": "hearts"}]

        input2 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer2 = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "eight", "suit": "hearts"},
                   {"rank": "eight", "suit": "spades"}]

        # Tricky test - program needs to go all the way through cards for this reason.
        input3 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"},
                  {"rank": "ace", "suit": "diamonds"}]

        answer3 = [{"rank": "ace", "suit": "clubs"},
                   {"rank": "ace", "suit": "diamonds"},
                   {"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"}]

        self.assertEqual(self.hand_ops.has_two_pair(input1), False)
        self.assertEqual(self.hand_ops.has_two_pair(input2), answer2)
        self.assertEqual(self.hand_ops.has_two_pair(input3), answer3)

    def test_has_trips(self):

        input1 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        input2 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer2 = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        input3 = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer3 = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        self.assertEqual(self.hand_ops.has_trips(input1), False)
        self.assertEqual(self.hand_ops.has_trips(input2), answer2)
        self.assertEqual(self.hand_ops.has_trips(input3), answer3)

    def test_has_quads(self):

        input1 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "eight", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        input2 = [{"rank": "ace", "suit": "clubs"},
                  {"rank": "queen", "suit": "clubs"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer2 = [{"rank": "queen", "suit": "clubs"},
                   {"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"}]

        self.assertEqual(self.hand_ops.has_quads(input1), False)
        self.assertEqual(self.hand_ops.has_quads(input2), answer2)

    def test_has_straight(self):

        input1 = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'three', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'clubs'}]

        input2 = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'clubs'}]

        input3 = [{'rank': 'ace', 'suit': 'clubs'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'six', 'suit': 'clubs'}]

        answer3 = [{'rank': 'six', 'suit': 'clubs'},
                   {'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'hearts'}]

        input4 = [{'rank': 'ace', 'suit': 'clubs'},
                  {'rank': 'deuce', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'spades'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'clubs'}]

        answer4 = [{'rank': 'five', 'suit': 'hearts'},
                   {'rank': 'four', 'suit': 'spades'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'hearts'},
                   {'rank': 'ace', 'suit': 'clubs'}]

        self.assertEqual(self.hand_ops.has_straight(input1), False)
        self.assertEqual(self.hand_ops.has_straight(input2), False)
        self.assertEqual(self.hand_ops.has_straight(input3), answer3)
        self.assertEqual(self.hand_ops.has_straight(input4), answer4)

    def test_has_flush(self):

        input1 = [{'rank': 'ace', 'suit': 'clubs'},
                  {'rank': 'three', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'spades'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'clubs'}]

        input2 = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'diamonds'}]

        answer2 = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'}]

        input3 = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'hearts'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'five', 'suit': 'hearts'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'seven', 'suit': 'diamonds'}]

        answer3 = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'seven', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'diamonds'}]

        self.assertEqual(self.hand_ops.has_flush(input1), False)
        self.assertEqual(self.hand_ops.has_flush(input2), answer2)
        self.assertEqual(self.hand_ops.has_flush(input3), answer3)

    def test_has_full_house(self):

        input1 = [{"rank": "eight", "suit": "clubs"},
                  {"rank": "eight", "suit": "hearts"},
                  {"rank": "eight", "suit": "diamonds"},
                  {"rank": "queen", "suit": "diamonds"},
                  {"rank": "queen", "suit": "spades"},
                  {"rank": "queen", "suit": "hearts"}]

        answer1 = [{"rank": "queen", "suit": "diamonds"},
                   {"rank": "queen", "suit": "hearts"},
                   {"rank": "queen", "suit": "spades"},
                   {"rank": "eight", "suit": "clubs"},
                   {"rank": "eight", "suit": "diamonds"}]

        self.assertEqual(self.hand_ops.has_full_house(input1), answer1)

    def test_has_straight_flush(self):
        input1 = [{'rank': 'queen', 'suit': 'diamonds'},
                  {'rank': 'nine', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'ten', 'suit': 'diamonds'}]

        answer1 = [{'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'queen', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'ten', 'suit': 'diamonds'},
                   {'rank': 'nine', 'suit': 'diamonds'}]

        input2 = [{'rank': 'queen', 'suit': 'diamonds'},
                  {'rank': 'nine', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'jack', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'ten', 'suit': 'diamonds'}]

        answer2 = [{'rank': 'ace', 'suit': 'diamonds'},
                   {'rank': 'king', 'suit': 'diamonds'},
                   {'rank': 'queen', 'suit': 'diamonds'},
                   {'rank': 'jack', 'suit': 'diamonds'},
                   {'rank': 'ten', 'suit': 'diamonds'}]

        input3 = [{'rank': 'ace', 'suit': 'diamonds'},
                  {'rank': 'nine', 'suit': 'diamonds'},
                  {'rank': 'three', 'suit': 'diamonds'},
                  {'rank': 'four', 'suit': 'diamonds'},
                  {'rank': 'deuce', 'suit': 'diamonds'},
                  {'rank': 'king', 'suit': 'diamonds'},
                  {'rank': 'five', 'suit': 'diamonds'}]

        answer3 = [{'rank': 'five', 'suit': 'diamonds'},
                   {'rank': 'four', 'suit': 'diamonds'},
                   {'rank': 'three', 'suit': 'diamonds'},
                   {'rank': 'deuce', 'suit': 'diamonds'},
                   {'rank': 'ace', 'suit': 'diamonds'}]

        self.assertEqual(self.hand_ops.has_straight_flush(input1), answer1)
        self.assertEqual(self.hand_ops.has_straight_flush(input2), answer2)
        self.assertEqual(self.hand_ops.has_straight_flush(input3), answer3)

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

if __name__=='__main__':
      unittest.main()
