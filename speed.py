from guts import HandOperations
import time
import random as r

# Speed test

hand_ops = HandOperations()

def speed_test(B):
    r.seed(1)
    start = time.time()
    royals, sflushes, quads, fhouses = 0, 0, 0, 0
    flushes, straights, trips, twopairs, pairs = 0, 0, 0, 0, 0
    for b in range(B):
        some_cards = r.sample(hand_ops.full_deck_of_cards, 7)
        if hand_ops.has_straight_flush(some_cards):
            sflushes += 1
            continue
        if hand_ops.has_quads(some_cards):
            quads += 1
            continue
        if hand_ops.has_full_house(some_cards):
            fhouses += 1
            continue
        if hand_ops.has_flush(some_cards):
            flushes += 1
            continue
        if hand_ops.has_straight(some_cards):
            straights += 1
            continue
        if hand_ops.has_trips(some_cards):
            trips += 1
            continue
        if hand_ops.has_two_pair(some_cards):
            twopairs += 1
            continue
        if hand_ops.has_pair(some_cards):
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