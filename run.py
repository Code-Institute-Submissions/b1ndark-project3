# import random, so cards can be shuffled in the game
import random
import os


# Function to clear screen
def clean():
    os.system("clear")


# Function to show instructions
def instructions():
    clean()
    print("*" * 40)
    print("\n            Instructions! \n")
    print("*" * 40)
    print("*" * 40)
    print("\n  Main goal is to either get 21 points\n\
    or to be as close as possible\n\
        \n  If you go above 21 you automatically\n\
             lose the game\n")
    print("    The dealer will ask you whether\n\
        you want to Hit or Stay\n")
    print("   2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6\n\
  7 = 7, 8 = 8, 9 = 9, J = 10, Q = 10\n\
    K = 10, and finally A = 1 or 11\n")
    print("  The main goal is to beat the dealer!\n")
    print("*" * 40)

    print("\nPlease select from the following options:")
    # While loop to loop through the try/except and if statements
    while True:
        number_entered = input("\n   1: Start.\n   2: Exit.\n")
        # Try/Except to check whether is a number or not
        try:
            number_entered = int(number_entered)
        except:
            print("\n****Invalid Input Entered****")
        # If statement to check what option user has selected
        if number_entered == 1:
            start()
            break
        elif number_entered == 2:
            mainMenu()
            break
        else:
            print("Please enter a number from the Selected options:")


class cards_deck:
    def __init__(self):
        self.cards = []
        # List of car suits
        card_suits = ["clubs", "diamonds", "hearts", "spades"]
        # Dictionary list with card ranks and their respective values 
        card_ranks = [
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

        # Append card_suits and card_ranks onto cards list 'cards = []'
        for card_suit in card_suits:
            for rank in card_ranks:
                self.cards.append([card_suit, rank])


    # To shuffle the cards list
    def shuffleCards(self):
        random.shuffle(self.cards)


    def deal_card(self, number):
        cards_dealt = []
        for i in range(number):

            card = self.cards.pop()
            cards_dealt.append(card)
        return cards_dealt

deck1 = cards_deck()
deck1.shuffleCards()
print(deck1.cards)


# Main Menu function where you will be able to select Instructions
# Or start the game
def mainMenu():
    clean()
    print("*" * 40)
    print("\n        Welcome to BlackJack Game \n")
    print("*" * 40)
    print("*" * 40)
    print("\nPlease select from the following options:")

    # While loop to loop through the try/except and if statements
    while True:
        number_entered = input("\n   1: Instructions.\n   2: Start.\n")
        # Try/Except to check whether is a number or not
        try:
            number_entered = int(number_entered)
        except:
            print("\n****Invalid Input Entered****")
        # If statement to check what option user has selected
        if number_entered == 1:
            instructions()
            break
        elif number_entered == 2:
            username()
            break
        else:
            print("Please enter a number from the Selected options:")


# mainMenu()

