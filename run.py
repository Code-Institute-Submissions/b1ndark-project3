# import random, so cards can be shuffled in the game
import random
import os

def clean():
    os.system("clear")

def instructions():
    clean()
    print("Hello")


# Variables
value = False
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
def shuffleCard():
    random.shuffle(cards)

def dealCard(number):
    cardsDealt = []
    card = cards.pop()
    return cardsDealt



# Main Menu function where you will be able to select Instructions or start the game
def mainMenu():
    clean()
    print("*" * 40)
    print("\n        Welcome to BlackJack Game \n")
    print("*" * 40)
    print("*" * 40)
    print("\nPlease select from the following options:")

    while (True):
        number_entered = input("\n   1: Instructions.\n   2: Start.\n")
        # Try/Except to check whether is a number or not
        try:
            number_entered = int(number_entered)
        except:
            print("****Invalid Input Entered****")
        # If statement to check what option user has selected
        if number_entered == 1:
            instructions()
            break
        elif number_entered == 2:
            username()
            break
        else:
            print("Please enter a number from the Selected options\n") 
    
mainMenu()

