''' Import random, so cards can be shuffled in the game, import os
to clear terminal and also import colorama to add colours to the game '''
import random
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)

'''
I have used some tutorials to help me build the Blackjack game
I will leave their links below:
https://www.youtube.com/watch?v=mpL0Y01v6tY&ab_channel=CodeCoach
https://www.youtube.com/watch?v=aryte85bt_M&t=140s&ab_channel=Beau%28previouslyZizyo%29
The next video to help me with the game rules:
https://www.youtube.com/watch?v=eyoh-Ku9TCI&ab_channel=wikiHow
'''

''' Variable '''
USERNAME = ""


def clean():
    '''
    This function when called will clear screen
    This is to improve User experience
    '''
    os.system("clear")


def instructions():
    '''
    This function will open instructions
    User will find the instructions and be able to understand the game
    There are two options Start/Exit
    I have used Try/except to check if a number has been entered or not
    '''
    clean()
    print("*" * 80)
    print(f"\n                   {USERNAME} welcome to the instructions! \n")
    print("*" * 80)
    print("\n       Main goal is to either get 21 points or\
 to be as close as possible\n\
              If you go above 21 you automatically lose the game\n")
    print("            The dealer will ask you whether you want\
 to Hit or Stay\n")
    print("         2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6, 7 = 7, 8 = 8,\
 9 = 9, J = 10\n\
                   Q = 10 K = 10, and finally A = 1 or 11\n")
    print("                     The main goal is to beat the dealer!\n")
    print("*" * 80)

    print("\n  Please select from the following options:")
    ''' While loop to loop through the try/except and if statements '''
    while True:
        numberEntered = input("\n     1: Start\n     2: Exit\n")
        ''' Try/Except to check whether is a number or not '''
        try:
            numberEntered = int(numberEntered)
        except Exception:
            print("\n         ****Invalid Input Entered****")
        ''' If statement to check what option user has selected '''
        ''' Loop will break once option is selected '''
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
    ''' init function to create an object in this case, to create a card '''
    def __init__(self, cardSuit, cardRank):
        self.cardSuit = cardSuit
        self.cardRank = cardRank

    ''' to create and return a readable string of the card '''
    def __str__(self):
        return f"    {self.cardRank['rank']} {self.cardSuit}"


class cardsDeck:
    def __init__(self):
        '''
        Here a cards deck of 52 cards will be created
        where they will be associated with the respective suit
        by appending them to a list of cards
        ♣ - clubs, ♦ - diamonds, ♥ - hearts, ♠ - spades
        '''
        self.cards = []
        ''' List of card suits '''
        cardSuits = ["♣", Fore.RED + "♦", Fore.RED + "♥", "♠"]
        ''' Dictionary list with card ranks and their respective values '''
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

        ''' Append cardSuits and cardRanks onto cards list 'cards = []' '''
        for cardSuit in cardSuits:
            for cardRank in cardRanks:
                self.cards.append(cardSelected(cardSuit, cardRank))

    def shuffleCards(self):
        '''
        To shuffle the cards list
        When shuffling cards it will check if there's more than one card left
        '''
        if len(self.cards) == 1:
            pass
        else:
            random.shuffle(self.cards)

    def dealCard(self, number):
        '''
        Function to deal cards, once they are dealt, they also will be popped
        And moved to cardsDealt
        '''
        cardsDealt = []
        for i in range(number):
            ''' To check whether there are any cards left to be removed '''
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

    def addCard(self, cardList):
        ''' Extend method to add each card to cardList '''
        self.cards.extend(cardList)

    def cardValueCalculate(self):
        ''' Function to check values and if there is an ace '''
        self.value = 0
        self.ace = False
        ''' Check the cards value and calculate the total of the same ones '''
        for card in self.cards:
            cardValueCalculate = int(card.cardRank["value"])
            self.value += cardValueCalculate
            ''' Checks for ace cards if they been dealt '''
            if card.cardRank["rank"] == "A":
                self.ace = True

        '''
        So if there is an Ace and the total score is above 21
        It will remove 10 score of the same Ace, example 22-10 = 12
        '''
        if self.ace is True:
            if self.value > 21:
                self.value -= 10

    def displayValue(self):
        '''
        This function will calculate the value of the
        cards that are displayed
        '''
        self.cardValueCalculate()
        return self.value

    def blackJack(self):
        '''
        Function will check if the total is 21
        and if it is, then is a Blackjack
        '''
        return self.displayValue() == 21

    def display(self, displayDealersHiddenCard=False):
        ''' Function to display the cards and their total value '''
        if self.cardDealer is True:
            ''' If is cardDealer, it will print this '''
            print(f'{"  Dealer cards are:"}')
        else:
            ''' Else if is the User, it will print this '''
            print(f'  {USERNAME} your cards are:')
        ''' Will print each card called '''
        for index, card in enumerate(self.cards):
            if index == 1 and self.cardDealer and not\
                 displayDealersHiddenCard and not self.blackJack():
                print("      🂠")
            else:
                print(card)
        ''' Checks if isn't the cardDealer '''
        if not self.cardDealer:
            print("  Total value of:", self.displayValue())

        print()


class blackJackGame:
    def playGame(self):
        '''
        This function will start the game
        The game will start with two cards dealt
        If there is no blackjack at the beginning,
        the user will be able to decide whether to hit or stay
        At the end the user will be able to decide if wants to play again
        or go back to main menu
        '''
        clean()
        print("*" * 80)
        print(f"\n                      {USERNAME} let's start the game! \n")
        print("*" * 80)
        print("*" * 80)

        ''' To shuffle the deck of cards for the game '''
        deck = cardsDeck()
        deck.shuffleCards()

        cardDealerHand = handCard(cardDealer=True)
        userHand = handCard()

        ''' to deal cards to the Dealer and the User from the shuffled deck '''
        for i in range(2):
            cardDealerHand.addCard(deck.dealCard(1))
            userHand.addCard(deck.dealCard(1))

        ''' Cards dealt will be printed '''
        print("\n")
        cardDealerHand.display()
        userHand.display()

        '''
         if statement to check if there are any winners
         as the first 2 cards are dealt
        '''
        self.winnerCheck(cardDealerHand, userHand)

        while userHand.displayValue() < 21 and \
                cardDealerHand.displayValue() < 21:
            print("  Please Select from below:")
            numberEntered = input("     1: Hit\n     2: Stay\n")
            while numberEntered not in ["1", "2"]:
                numberEntered = input("\n  Please enter:\n     1: Hit\n\
     2: Stay\n")
            '''
            Try/Except to check whether is a number or not
            If statement to check what option user has selected
            Loop will break once option is selected
            '''
            try:
                numberEntered = int(numberEntered)
            except Exception:
                print("\n        ****Invalid Input Entered****")
            if numberEntered == 1:
                cardDealerHandValue = cardDealerHand.displayValue()
                userHandValue = userHand.displayValue()
                ''' This will add a card to the dealer if total is < 17 '''
                if cardDealerHandValue < 17:
                    cardDealerHand.addCard(deck.dealCard(1))
                    cardDealerHandValue = cardDealerHand.displayValue()
                ''' Add card to User '''
                userHand.addCard(deck.dealCard(1))
                cardDealerHand.display()
                userHand.display()
            elif numberEntered == 2:
                cardDealerHandValue = cardDealerHand.displayValue()
                userHandValue = userHand.displayValue()
                ''' This will add a card to the dealer if total is < 17 '''
                while cardDealerHandValue < 17:
                    cardDealerHand.addCard(deck.dealCard(1))
                    cardDealerHandValue = cardDealerHand.displayValue()
                break

        print()
        print("*" * 80)
        print(f"\n                         Blackjack Game is over\n")
        print("*" * 80)
        print()
        cardDealerHand.display(displayDealersHiddenCard=True)
        userHand.display()
        self.winnerCheck(cardDealerHand, userHand, gameOver=True)
        print()
        print("*" * 80)
        print("  Please select from the following options:")

        '''
        While loop to loop through the try/except and if statements
        Try/Except to check whether is a number or not
        If statement to check what option user has selected
        Loop will break once option is selected
        '''
        while True:
            numberEntered = input("     1: Main Menu\n\
     2: Play again\n")
            try:
                numberEntered = int(numberEntered)
            except Exception:
                print("\n            ****Invalid Input Entered****")
            if numberEntered == 1:
                mainMenu()
                break
            elif numberEntered == 2:
                game = blackJackGame()
                game.playGame()
                break
            else:
                print("  Please select a number from the options:")

    def winnerCheck(self, cardDealerHand, userHand, gameOver=False):
        '''
        This function will check for winner, whether is the cardDealer
        or the user, if there is a draw, blackjack and if someone has bust
        '''
        if not gameOver:
            if userHand.displayValue() > 21:
                print(f"  {Fore.RED}{USERNAME} you bust!")
                return True
            elif cardDealerHand.displayValue() > 21:
                print(f"  {Fore.GREEN}Dealer has bust!\
                \n  {USERNAME} you have won!")
                return True
            elif cardDealerHand.blackJack() and userHand.blackJack():
                print(f"  {Fore.RED}No Winners\n  It's a tie!")
                return True
            elif cardDealerHand.blackJack():
                print(f"  {Fore.RED}{USERNAME} you have lost!")
                return True
            elif userHand.blackJack():
                print(f"  {Fore.GREEN}Dealer has lost!\
                \n  {USERNAME} you have a Blackjack!")
                return True
        else:
            if userHand.displayValue() > 21:
                print(f"  {Fore.RED}{USERNAME} you bust!")
            elif cardDealerHand.displayValue() > 21:
                print(f"  {Fore.GREEN}Dealer has bust!\
                \n  {USERNAME} you have won!")
            elif userHand.displayValue() > cardDealerHand.displayValue():
                print(f"  {Fore.GREEN}Dealer has lost!\
                \n  {USERNAME} you have won!")
            elif cardDealerHand.displayValue() == userHand.displayValue():
                print(f"  {Fore.RED}No winners.\n  It's a tie!")
            else:
                print(f"  {Fore.RED}{USERNAME} you have lost!")
            return True
        return False


def mainMenu():
    '''
    Main Menu function where you will be able to select Instructions
    Or start the game
    While loop to loop through the try/except and if statements
    '''
    clean()
    print("*" * 80)
    print(f"\n                  {USERNAME} welcome to Blackjack Game \n")
    print("*" * 80)
    print("*" * 80)
    print("\n  Please select from the following options:")

    while True:
        numberEntered = input("\n     1: Instructions\n     2: Start\n")
        ''' Try/Except to check whether is a number or not '''
        try:
            numberEntered = int(numberEntered)
        except Exception:
            print("\n         ****Invalid Input Entered****")
        '''
        If statement to check what option user has selected
        Loop will break once option is selected
        '''
        if numberEntered == 1:
            instructions()
            break
        elif numberEntered == 2:
            game = blackJackGame()
            game.playGame()
            break
        else:
            print("  Please select a number from the options:")


def userName():
    '''
    This function will ask the user to type the username
    While loop to loop through the if statements
    To check whether username has been entered or not
    '''
    clean()
    print("*" * 80)
    print("\n                        Welcome to Blackjack Game \n")
    print("*" * 80)
    print("*" * 80)
    '''
    Check for spaces, for blank input, if user entered symbols or numbers
    '''
    while True:
        global USERNAME
        USERNAME = input("\n  Please enter your username:\n")
        if USERNAME.isspace() is True:
            print("  Please enter username in order to proceed")
        elif USERNAME == "":
            print("  Please enter username in order to proceed")
        elif USERNAME.isalpha() is False:
            print("  Only letters accepted")
        else:
            mainMenu()
            break


userName()
