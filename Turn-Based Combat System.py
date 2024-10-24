import tbc

class Character(object):
    def __int__(self, name = “Axolot”, hitPoints=0, hitChance=0, maxDamage=0, armor=0):
super() . __init__()
self.name = name
self.hitPoints = hitPoints
self.hitChance = maxDamage
self.armor = armor

 def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out


@property
def name(self):
	return self.__name__

@name.setter
def name(self, value):
	self.__name = value

@property
def hitPoint(self):
    return self.__hitPoint__

@hitPoint.setter
def hitPoint(self, value):
    return self.__hitPoint = value

@property
def hitChance(self):
    return self.__hitChance__

@hitChance.setter
def hitChance(self, value):
    return self.__hitChance = value


@property
def armor(self):
Return self.__armor

def printStats(self):
        print(f"""
        {self.name}
        ===================
        Hit points: {self.hitPoints}
        Hit chance: {self.hitChance}
        Maximum damage: {self.maxDamage}
        Armor rating: {self.armor}
            """)

def hit(self, enemy)
If random.randint(1, 100) < self.hitPerc:
	Print (f”{self.name} hits {enemy.name}...”)
damage = random.randint(1, self.maxDamage)
           print (f"for {damage} damage.")
           damage -= enemy.armor
           if enemy.armor > 0:
                print(f"{enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            damage = 0
            print(f"{self.name} missed, dealing {damage} damage.")
        return damage


def basicFight(player1, player2):
keepGoing = True
While keepGoing:
	player1.hit(player2)
	player2.hit(player1)

print (f”{player1.name} HP: {player1.hitPoint}”)
print (f”{player2.name} HP: {player2.hitPoint}”)
print ()
	
	If player1.hitPoints <= 0:
print (f”{player1.name} has lost”)
keepGoing = False:
elIf player2.hitPoints <= 0:
print (f”{player2.name} has lost”)
keepGoing = False
