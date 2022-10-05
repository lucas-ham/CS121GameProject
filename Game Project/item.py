import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, type, cost=0,damage=0):
        self.name = name
        self.desc = desc
        self.loc = None
        self.cost = cost
        self.damage = damage
        self.type = type
    def describe(self):
        #updated describe method to account for different types of items
        #allowed for rephrasing of the sentences
        if self.type == "weapon":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is a weapon. It does" ,self.damage,"damage to foes\n")
            input("Press enter to continue...")
        elif self.type == "defense":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is a defensive object. It has a" , str(self.damage)+"% chance of blocking an attack\n")
            input("Press enter to continue...")
        elif self.type == "heal":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is a healing object. It can be used once")
            print("When used, this item will heal you for "+str(self.damage)+" damage\n")
            input("Press enter to continue...")
        elif self.type == "spell":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is a spell object. It can be used once")
            print("When used, this item will add",self.damage,"spell points to you")
            input("Press enter to continue...")
        elif self.type == "ex":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is an expirience object. It can be used once")
            print("When used, this item will add",self.damage,"expirience points")
            input("Press enter to continue...")
        elif self.type == "win":
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is one of three special objects, collect all three to kill all the monsters and win the game!")
            input("Press enter to continue...")
        else:
            clear()
            print(str(self.desc)+". This is worth a retail price of",self.cost,"\n")
            print("This is a standard weapon. It has no benefit in battle\n")
            input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
