import pygame, simpleGE, random

NUMCARD = 20

DECK = 0
HAND = 1
DISCARD = 2

STATES = ("deck", "hand", "discard")

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.cardSlot = CardSlot(self)
        self.cardSlot.position = (320, 240)
        
        self.setupCards()
        
        self.sprites = [self.cardSlot]
        
    def setupCards(self):
        self.cards = []
        for cn in range(NUMCARDS):
            self.cards.append(Card(cn))

class CardSlot(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("abstract_clouds.png")
        
    def process(self):        
        if self.clicked:
            cardNum = random.randrange(DECK)
            currentCard = self.scene.cards[cardNum]
            self.copyImage(currentCard.image)

class Character(object):
    def __init__(self, name, hp):
        super().__init__()
        self.name = name
        self.hp = hp
        self.shield = 0
        
    def report(self):
        print(f"""
        {self.name}
        hp: {self.hp}
        shield: {self.shield}
        """)
        
    def apply(self, card):
        self.hp -= card.damage
        self.shield += card.shield

class lblHealth(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
      def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)                
class Card(object):
    def __init__(self, name, damage, shield):
        self.name = name
        self.damage = damage
        self.shield = shield
        self.state = DECK
        
    def apply(self, character):
        character.hp -= damage
        character.shield += shield
        
    def display(self):
        print(f"""
        {self.name} 
        damage amount: {self.damage}
        shield amount: {self.shield}    
        """)
        
    def displayShort(self):
        location = STATES[self.state]
        print(f"{self.name:15} ({location:^7}) D: {self.damage:<3} S: {self.shield}")
        
class Fighter(Card):
    def __init__(self):
        super().__init__("Fighter", 3, 0)
        
class ShieldBearer(Card):
    def __init__(self):
        super().__init__("ShieldBearer", 0, 3)
        
class Healer(Card):
    def __init__(self):
        super().__init__("Healer", -2, 0)

class Witch(Card):
    def __init__(self):
        super().__init__("Witch", -1, 0)

class Archer(Card):
    def __init__(self):
        super().__init__("Archer", 2, 1)
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.setDefaultDeck()
        
    def setDefaultDeck(self):
        self.cards.append(Fighter())
        self.cards.append(ShieldBearer())
        self.cards.append(Healer())
        self.cards.append(Fighter())
        self.cards.append(ShieldBearer())
        
    def showDeck(self):
        for card in self.cards:
            if card.state == DECK:
                card.display()

    def showHand(self):
        for card in self.cards:
            if card.state == HAND:
                card.display()
                
    def showDiscard(self):
        for card in self.cards:
            if card.state == DISCARD:
                card.display()

    def showAllCards(self):
        for card in self.cards:
            card.displayShort()
        print()

    def shuffle(self):
        """ return cards in discard back to deck """
        print("shuffling...")
        for card in self.cards:
            if card.state == DISCARD:
                card.state = DECK

    def cardsInDeck(self):
        cardsLeft = 0
        for card in self.cards:
            if card.state == DECK:
                cardsLeft += 1
        return cardsLeft
    
    def discard(self, cardNum):
        hand = []
        for card in self.cards:
            if card.state == HAND:
                hand.append(card)
                
        currentCard = hand[cardNum]
        currentCard.state = DISCARD

    def deal(self, numCards):
        for cardNum in range(numCards):
            # reshuffle if necessary
            if self.cardsInDeck() <= 0:
                self.shuffle()

            keepGoing = True
            while keepGoing:
                currentCard = random.choice(self.cards)        
                if currentCard.state == DECK:
                    currentCard.state = HAND
                    keepGoing = False

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
