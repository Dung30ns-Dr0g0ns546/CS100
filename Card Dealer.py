# Main:
# 	initialize cardDB [initCards()]
# 	Assign five cards to player [assignCard()]
# 	Assign five cards to computer via assignCard()

# 	Show the current deck [showDB()]

# 	Show cards in player hand [showHand]
# 	Show cards in computer hand via showHand()



# initCard [create list, indices 0-51, values all = 0, return cardDB]
# showDB [takes cardDB as parameter, for each element in cardDB (Print id, location noe, convert id to card name, convert location with HANDS later), no return value is needed]
# getCardName [not in main, takes cardID as parameter, uses // and % to get rank and suit IDS, uses RANKNAME and SUITNAME, ]
# assignCard [takes cardDB and hand as parameters, get random cardID 0-51, assign hand to that card, no return value is needed]
# showHand [takes cardDB and hand as parameters, go through cardDB (if location is hand = print card name), No return value is needed]



""" cards.py
    demonstrates functions
    manage a deck of cards db

"""

import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

def initCards():
    """
    No parameters
    Creates an empty list called cardDB
    Assign 52 entries, all zeros
    Retur cardDB
    """
    
    cardDB = []
    for i in range(NUMCARDS):
        cardDB.append(0)
    return cardDB

def showDB (cardDB):
    """
    takes cardDB as parameter
    for each element in cardDB
        Print id
        location noe
        convert id to card name
        convert location with HANDS
    No return value
    """
    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum:3} : {getCardName(cardNum):25} {HANDS[location]}")
    print()

def getCardName(cardNum):
    """
    Parameters: cardNum
    Integer divide cardNum by 13 -> suit
    Modulus of cardNum and 13 -> rank
    Use SUITNAME and RANKNAME tuples to get a string name
    Return card name
    """
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = f"{RANKNAME[rank]} of {SUITNAME[suit]}"
    return cardName

def assignCard(cardDB, hand):
    """
    Parameters: cardDB, hand
    Pick a random number 0 - 51
    Assign hand to that numers location
    (how do we make sure same card isn't chosen twice?)
    No return value needed
    """
    cardNum = random.randrange(NUMCARDS)
    cardDB[cardNum] = hand
    
def showHand(cardDB, hand):
    """
    Parameters: cardDB, hand
    Step through all cards
        If card is in hand
            Print card name
    No return value
    """
    print(f"Cards in {HANDS[hand]} hand")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print (f"{getCardName(cardNum)}")
            
    print()
    
main()