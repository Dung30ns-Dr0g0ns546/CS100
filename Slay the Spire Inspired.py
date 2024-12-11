import pygame, simpleGE, random

NUMCARD = 20

DECK = 0
HAND = 1
DISCARD = 2

STATES = ("deck", "hand", "discard")

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

class Dice(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Dice Faces/dice-six-faces-one.svg")
        self.setSize(50, 50)
        
        self.images = [None,
                       pygame.image.load("Dice Faces/dice-six-faces-one.svg"),
                       pygame.image.load("Dice Faces/dice-six-faces-two.svg"),
                       pygame.image.load("Dice Faces/dice-six-faces-three.svg"),
                       pygame.image.load("Dice Faces/dice-six-faces-four.svg"),
                       pygame.image.load("Dice Faces/dice-six-faces-five.svg"),
                       pygame.image.load("Dice Faces/dice-six-faces-six.svg"),
                       ]
        for i in range(1, 7):
            self.images[i] = pygame.transform.scale(self.images[i], (50, 50))
                    
    def roll(self):
        self.value = random.randint(1, 6)
        self.copyImage(self.images[self.value])
        if self.value == 3:
            self.nRoll = 2
        elif self.value == 5:
            self.nRoll = 4
        else:
            self.nRoll = 0
        
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
                    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("forest.jpg")
        
        self.sndRoll = simpleGE.Sound("demos_petals_diceRoll.wav")
        pygame.mixer.music.load("demos_petals_bgm.mp3")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        
        self.lblName1 = simpleGE.Label()
        self.lblName1.text = "Name 1"
        self.lblName1.center = (80, 100)
        
        self.lblName2 = simpleGE.Label()
        self.lblName2.text = "Name 2"
        self.lblName2.center = (540, 100)
        
        self.lblHP1 = simpleGE.Label()
        self.lblHP1.text = "Hit Points 1"
        self.lblHP1.center = (80, 150)
        
        self.lblHP2 = simpleGE.Label()
        self.lblHP2.text = "Hit Points 2"
        self.lblHP2.center = (540, 150)
        
        self.btnRoll = simpleGE.Button()
        self.btnRoll.text = "Roll"
        self.btnRoll.center = (320,200)
        
        self.btnAttack = simpleGE.Button()
        self.btnAttack.text = "Attack"
        self.btnAttack.center = (320, 400)
        
        self.sprites = [self.lblName1,
                        self.lblName2,
                        self.lblHP1,
                        self.lblHP2,
                        self.btnRoll,
                        self.btnAttack]
        
    def process(self):
        if self.btnRoll.clicked:
            self.rollAll()
        
    def rollAll(self):
        self.sndRoll.play()
        for die in self.dice:
            die.roll()
            rollNumber += die.nRoll
            
        self.lblResult.text = f"You rolled a {rollNumber}"
        
        if self.lblResult.center[0] >= 0:
            self.lblResult.hide()
                

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
