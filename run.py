# import random so cards can be shuffled in the game
import random


# Variables
cards = []
card_suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = [
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10},
    {"rank": "A", "value": 11},
]

# Append card_suits and ranks onto cards list 'cards = []'
for card_suit in card_suits:
    for rank in ranks:
        cards.append([card_suit, rank])

# To shuffle the cards list
random.shuffle(cards)
print(cards[3])