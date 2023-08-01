# import random, so cards can be shuffled in the game
import random
# import os to clear terminal
import os

# Variable
USERNAME = ""


# Function to clear screen
def clean():
    os.system("clear")


# Function to show instructions
def instructions():
    clean()
    print("*" * 50)
    print(f"\n   {USERNAME} welcome to the instructions! \n")
    print("*" * 50)
    print("*" * 50)
    print("\n    Main goal is to either get 21 points\n\
      or to be as close as possible\n\
        \n    If you go above 21 you automatically\n\
               lose the game\n")
    print("      The dealer will ask you whether\n\
          you want to Hit or Stay\n")
    print("     2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6\n\
    7 = 7, 8 = 8, 9 = 9, J = 10, Q = 10\n\
      K = 10, and finally A = 1 or 11\n")
    print("    The main goal is to beat the dealer!\n")
    print("*" * 50)

    print("\n  Please select from the following options:")
    # While loop to loop through the try/except and if statements
    while True:
        numberEntered = input("\n     1: Start\n     2: Exit\n")
        # Try/Except to check whether is a number or not
        try:
            numberEntered = int(numberEntered)
        except:
            print("\n         ****Invalid Input Entered****")
        # If statement to check what option user has selected
        # Loop will break once option is selected
        if numberEntered == 1:
            game = blackJackGame()
            game.playGame()
            break
        elif numberEntered == 2:
            mainMenu()
            break
        else:
            print("  Please select a number from the options:")


class cardSelected:
    # init function to create an object in this case, to create a card
    def __init__(self, cardSuit, cardRank):
        self.cardSuit = cardSuit
        self.cardRank = cardRank

    # to create and return a readable string of the card
    def __str__(self):
        return f"    {self.cardRank['rank']} {self.cardSuit}"


class cardsDeck:
    def __init__(self):
        self.cards = []
        # List of card suits
        cardSuits = ["♣", "♦", "♥", "♠"]
        # Dictionary list with card ranks and their respective values
        cardRanks = [
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

        # Append cardSuits and cardRanks onto cards list 'cards = []'
        for cardSuit in cardSuits:
            for cardRank in cardRanks:
                self.cards.append(cardSelected(cardSuit, cardRank))

    # To shuffle the cards list
    def shuffleCards(self):
        # When shuffling cards it will check if theres more than one left
        if len(self.cards) == 1:
            pass
        else:
            random.shuffle(self.cards)

    # Function to deal cards, once they are dealt they also will be popped
    # And moved to cardsDealt
    def dealCard(self, number):
        cardsDealt = []
        for i in range(number):
            # To check whether there are any cards left to be removed
            if len(self.cards) == 0:
                pass
            else:
                card = self.cards.pop()
                cardsDealt.append(card)
        return cardsDealt


class handCard:
    def __init__(self, cardDealer=False):
        self.cards = []
        self.value = 0
        self.cardDealer = cardDealer

    # Extend method to add each card to cardList
    def addCard(self, cardList):
        self.cards.extend(cardList)

    # Funtion to check values and if there is an ace
    def cardValueCalculate(self):
        self.value = 0
        self.ace = False
        # Will check the cards value and calculate the total of the same ones
        for card in self.cards:
            cardValueCalculate = int(card.cardRank["value"])
            self.value += cardValueCalculate
            # Checks for ace cards if they been dealt
            if card.cardRank["rank"] == "A":
                self.ace = True

        # So if there is an Ace and the total score is above 21
        # It will remove 10 score of the same Ace, example 22-10 = 12
        if self.ace is True:
            if self.value > 21:
                self.value -= 10

    # To calculate the value of the cards
    def displayValue(self):
        self.cardValueCalculate()
        return self.value

    # If is 21 then is a BlackJack
    def blackJack(self):
        return self.displayValue() == 21

    # Function to display the cards and their total value
    def display(self, displayDealersHiddenCard=False):
        if self.cardDealer is True:
            # If is cardDealer, it will print this
            print(f'{"  Dealer cards are:"}')
        else:
            # Else if is the User, it will print this
            print(f'  {USERNAME} your cards are:')
        # Will print each card called
        for index, card in enumerate(self.cards):
            if index == 1 and self.cardDealer and not\
                 displayDealersHiddenCard and not self.blackJack():
                print("      🂠")
            else:
                print(card)
        # Checks if isn't the cardDealer
        if not self.cardDealer:
            print("  Total value of:", self.displayValue())

        print()


class blackJackGame:
    def playGame(self):
        clean()
        print("*" * 40)
        print(f"\n     {USERNAME} let's start the game! \n")
        print("*" * 40)
        print("*" * 40)

        # To shuffle the deck of cards for the game
        deck = cardsDeck()
        deck.shuffleCards()

        cardDealerHand = handCard(cardDealer=True)
        userHand = handCard()

        # to deal cards to the Dealer and the User from the shuffled deck
        for i in range(2):
            cardDealerHand.addCard(deck.dealCard(1))
            userHand.addCard(deck.dealCard(1))

        # Cards dealt will be printed
        print("\n")
        cardDealerHand.display()
        userHand.display()

        # if statement to check if there is any winners
        # as the first 2 cards are dealt
        self.winnerCheck(cardDealerHand, userHand)

        while userHand.displayValue() < 21 and \
                cardDealerHand.displayValue() < 21:
            print("  Please Select from below:")
            numberEntered = input("     1: Hit\n     2: Stay\n")
            while numberEntered not in ["1", "2"]:
                numberEntered = input("\n  Please enter:\n     1: Hit\n\
     2: Stay\n")
            # Try/Except to check whether is a number or not
            try:
                numberEntered = int(numberEntered)
            except:
                print("\n        ****Invalid Input Entered****")
            # If statement to check what option user has selected
            # Loop will break once option is selected
            if numberEntered is 1:
                cardDealerHandValue = cardDealerHand.displayValue()
                userHandValue = userHand.displayValue()
                # This will add a card to the dealer if total is < 17
                if cardDealerHandValue < 17:
                    cardDealerHand.addCard(deck.dealCard(1))
                    cardDealerHandValue = cardDealerHand.displayValue()
                # Add card to User
                userHand.addCard(deck.dealCard(1))
                cardDealerHand.display()
                userHand.display()
                
            elif numberEntered is 2:
                cardDealerHandValue = cardDealerHand.displayValue()
                userHandValue = userHand.displayValue()
                # This will add a card to the dealer if total is < 17
                while cardDealerHandValue < 17:
                    cardDealerHand.addCard(deck.dealCard(1))
                    cardDealerHandValue = cardDealerHand.displayValue()
                # To check if there is any winners
                
                break
        self.winnerCheck(cardDealerHand, userHand, gameOver=True)
        print()
        print("*" * 50)
        print("*" * 50)
        print(f"\n              BlackJack Game is over\n")
        print("*" * 50)
        print()
        cardDealerHand.display(displayDealersHiddenCard=True)
        userHand.display()
        print()
        print("*" * 50)
        print("*" * 50)
        print("\n  Please select from the following options:")
        # While loop to loop through the try/except and if statements
        while True:
            numberEntered = input("\n     1: Main Menu\n\
     2: Play again\n")
            # Try/Except to check whether is a number or not
            try:
                numberEntered = int(numberEntered)
            except:
                print("\n         ****Invalid Input Entered****")
            # If statement to check what option user has selected
            # Loop will break once option is selected
            if numberEntered == 1:
                mainMenu()
                break
            elif numberEntered == 2:
                game = blackJackGame()
                game.playGame()
                break
            else:
                print("  Please select a number from the options:")

    # Function to check if there is a winner or a tie
    def winnerCheck(self, cardDealerHand, userHand, gameOver=False):
        if not gameOver:
            if userHand.displayValue() > 21:
                print(f"  {USERNAME} you bust!")
                return True
            elif cardDealerHand.displayValue() > 21:
                print(f"  Dealer has bust!\n  {USERNAME} you have won!")
                return True
            elif cardDealerHand.blackJack() and userHand.blackJack():
                print("  No Winners\n  It's a tie!")
                return True
            elif cardDealerHand.blackJack():
                print(f"  {USERNAME} you have lost!")
                return True
            elif userHand.blackJack():
                print(f"  Dealer has lost!\n  {USERNAME} you have won!")
                return True
        else:
            if userHand.displayValue() > 21:
                print(f"  {USERNAME} you bust!")
            elif cardDealerHand.displayValue() > 21:
                print(f"  Dealer has bust!\n  {USERNAME} you have won!")
            elif userHand.displayValue() > cardDealerHand.displayValue():
                print(f"  Dealer has lost!\n  {USERNAME} you have won!")
            elif cardDealerHand.displayValue() == userHand.displayValue():
                print("  No winners.\n  It's a tie!")
            else:
                print(f"  {USERNAME} you have lost!")
            return True
        return False


# Main Menu function where you will be able to select Instructions
# Or start the game
def mainMenu():
    clean()
    print("*" * 50)
    print(f"\n      {USERNAME} welcome to BlackJack Game \n")
    print("*" * 50)
    print("*" * 50)
    print("\n  Please select from the following options:")

    # While loop to loop through the try/except and if statements
    while True:
        numberEntered = input("\n     1: Instructions\n     2: Start\n")
        # Try/Except to check whether is a number or not
        try:
            numberEntered = int(numberEntered)
        except:
            print("\n         ****Invalid Input Entered****")
        # If statement to check what option user has selected
        # Loop will break once option is selected
        if numberEntered == 1:
            instructions()
            break
        elif numberEntered == 2:
            game = blackJackGame()
            game.playGame()
            break
        else:
            print("  Please select a number from the options:")


# This function will ask the user to type the username
def userName():
    clean()
    print("*" * 50)
    print("\n           Welcome to BlackJack Game \n")
    print("*" * 50)
    print("*" * 50)

    # While loop to loop through the try/except and if statements
    # To check whether username has been entered or not
    while True:
        global USERNAME
        USERNAME = input("\n  Please enter your username:\n")
        # Check for spaces
        if USERNAME.isspace() is True:
            print("  Please enter username in order to proceed")
        # Check for blank input
        elif USERNAME == "":
            print("  Please enter username in order to proceed")
        # Check if user entered symbols or numbers
        elif USERNAME.isalpha() is False:
            print("  Only letters accepted")
        else:
            mainMenu()
            # Had to add this break to stop the loop
            break


userName()
