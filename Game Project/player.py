import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.specialItems = []
        self.health = 50
        self.alive = True
        self.currency = 10

        #leveling up information
        #every time level up, healthCapastiy, spellPointCapasity, and fistDamage increase
        self.level = 1
        self.maxLevel = 10
        self.ex = 0
        self.levelUpEx = 15

        self.healthCapasity = 50
        self.maxHealth = 100

        #info on max items that can hold
        #increases with player level too
        self.itemCapasity = 10
        self.maxItems = 20

        #weapon info, will use fists if no weapon
        self.fistDamage = 2
        self.maxFistDamage = 7
        self.weapon = None

        #armor info, don't need to have one
        self.armor = None
        self.focusBenefit = 10
        self.focusLength = 3

        #spell info, storing costs etc here makes easier to change without worry of missing one
        self.spellPoints = 3
        self.spellPointCapasity = 5
        self.maxSpellPoints = 10

        self.smallSpellDamage = 5
        self.smallSpellCost = 1
        self.medSpellDamage = 20
        self.medSpellCost = 3
        self.largeSpellDamage = 50
        self.largeSpellCost = 5

    def goDirection(self, direction):
        newLoc = self.location.getDestination(direction)
        if newLoc:
            self.location = newLoc
            return True
        else:
            return False
    def pickup(self, item):
        if item.type == "win":
            self.specialItems.append(item)
            item.loc = self
            self.location.removeItem(item)
            if len(self.specialItems) > 2:
                clear()
                print("You have won the game")
                print("By gathering all of the three special ingredients, the monsters have all been killed")
                print("Thanks for playing!")
                self.alive = False
            else:
                print("Successfully picked up",item.name)
                print("You now have",len(self.specialItems))
                input("Press enter to continue...")
        elif len(self.items) < self.itemCapasity:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            print("Successfully picked up",item.name)
            input("Press enter to continue...")
        else:
            print("You are already holding the maximum number of items")
            print("Please drop items to pickup this item")
            input("Press enter to continue...")
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        #using a dictionary lets me combine multiple identical items
        itemDict = {}
        for i in self.items:
            if self.weapon != None and i.name == self.weapon.name:
                val = itemDict.get(i.name+" (weapon)",0)
                itemDict[i.name+" (weapon)"] = val + 1
            elif self.armor != None and i.name == self.armor.name:
                val = itemDict.get(i.name+" (armor)",0)
                itemDict[i.name+" (armor)"] = val + 1
            else:
                val = itemDict.get(i.name,0)
                itemDict[i.name] = val + 1

        #then use compiled dictionary of items to print
        #maybe faster to store this dictionary and update every time you pickup/buy an item?
        #unless lots of items, not that complicated to recalculate, but could reduce
        keys = list(itemDict.keys())
        vals = list(itemDict.values())
        for i in range(len(keys)):
            print(str(keys[i])+":",vals[i])
        print()
        print("You are holding",len(self.items),"items. You can hold a maximum of",self.itemCapasity,"items at one time")
        print()
        input("Press enter to continue...")

    #used for interacting with merchant
    def addCurrency(self,amount):
        self.currency += amount
    def removeCurrency(self,amount):
        self.currency -= amount
    def addHealth(self,amount):
        self.health = min(self.health + amount,self.healthCapasity)
    def addSpellPoints(self,amount):
        self.spellPoints = min(self.spellPoints + amount, self.spellPointCapasity)
    def buyItem(self,item):
        if self.currency >= item.cost:
            self.removeCurrency(item.cost)
            self.items.append(item)
            item.loc = self
    def sellItem(self,item,buyPrice):
        useItem = self.findItemByObject(item)
        self.items.remove(useItem)
        self.addCurrency(buyPrice)
        useItem.loc = "Merchant"
    def checkNumber(self,itemObj):
        count = 0
        for i in self.items:
            if i.name == itemObj.name:
                count+=1
        return count
    def checkWeaponArmor(self,itemName):
        useItem = self.findItemByName(itemName)
        if self.checkNumber(useItem) <= 1:
            if self.weapon != None and useItem.name == self.weapon.name:
                return True
            elif self.armor != None and useItem.name == self.armor.name:
                return True
        return False
    def discardItem(self,item):
        useItem = self.findItemByName(item)
        self.items.remove(useItem)
        useItem.loc = self.location
    def showStatus(self):
        clear()
        print("Your current stats are:")
        print()
        print("Health: ", self.health,"  Max Health at Current level:", self.healthCapasity)
        print()
        print("Currency: ", self.currency)
        print()
        print("Spell Capasity: ", self.spellPoints,"  Max spells at current level:",self.spellPointCapasity)
        print()
        print("Current Level:",self.level)
        print()
        print("Current EX points:",self.ex,"Points to level up:",self.levelUpEx-self.ex)
        print()
        print("Current special pieces collected:",len(self.specialItems),"  Special pieces to collect:",3-len(self.specialItems))
        print()

        #accounting for fists/weapons
        if self.weapon is not None:
            print("You have",self.weapon.name,"equiped as your weapon. It does",self.weapon.damage,"damage")
        else:
            print("In a battle you will fight with your fists unless you equip a weapon")
            print("Your fists do",self.fistDamage,"damage")

        #displays armor info if applicable
        if self.armor is not None:
            print()
            print("You are wearing", self.armor.name,"as armor. It has a "+str(self.armor.damage)+"% chance of blocking an attack")


        print()
        input("Press enter to continue...")
    def setWeapon(self,weaponName):
        #assumes input that player has and exists
        #this is cleaned by the main.py file
        useWeapon = self.findItemByName(weaponName)
        if useWeapon.type.lower() == "weapon":
            self.weapon = self.findItemByName(weaponName)
            print("Successfully equiped",self.weapon.name,"as weapon")
        else:
            print("Item not equiped, you can only use weapons to attack")
        input("Press enter to continue...")
    def setArmor(self,armorName):
        #also assumes player has item, for same reason
        useArmor = self.findItemByName(armorName)
        if useArmor.type.lower() == "defense":
            self.armor = useArmor
            print("Successfully equiped",self.armor.name,"as armor")
        else:
            print("Item not equiped, you can only equip defensive items as armor")
        input("Press enter to continue...")
    def checkForItem(self,item):
        #used throughout, checks if player has item (by name)
        for i in self.items:
            if item == i.name.lower():
                return True
        else:
            return False
    def findItemByObject(self,item):
        #name specifies, gets you where that object is in inventory
        for i in self.items:
            if item.name.lower() == i.name.lower():
                return i
    def findItemByName(self,itemName):
        #gets you the object from the name, if user has that item
        #used a lot for input-scenarios
        #user wants to equip item y, finds the object with name y
        for i in self.items:
            if itemName.lower() == i.name.lower():
                return i
    def updateLevel(self):
        if self.ex >= self.levelUpEx and self.level < self.maxLevel:
            #this deals with leveling up the player
            #changes the things that need to change so they will max out at max level
            levelsUp = 0
            while self.ex >= self.levelUpEx and self.level < self.maxLevel:
                if self.level == self.maxLevel - 1:
                    self.healthCapasity = self.maxHealth
                    self.spellPointCapasity = self.maxSpellPoints
                    self.fistDamage = self.maxFistDamage
                    self.itemCapasity = self.maxItems
                    self.ex = 0
                    self.level = self.maxLevel
                elif self.level % 2 == 0:
                    self.healthCapasity += (self.maxHealth - self.healthCapasity)//(self.maxLevel - self.level)
                    self.spellPointCapasity +=1
                    self.itemCapasity += 1
                    self.ex -=self.levelUpEx
                    self.level +=1
                    levelsUp +=1
                else:
                    self.healthCapasity += (self.maxHealth - self.healthCapasity)//(self.maxLevel - self.level)
                    self.fistDamage += 1
                    self.itemCapasity +=1
                    self.ex -= self.levelUpEx
                    self.level += 1
                    levelsUp +=1
            if self.level == self.maxLevel:
                print()
                print("You have reached the maximum level!")
                print("You now have a max health of",self.healthCapasity)
                print("You now have a max spell capasity of",self.spellPointCapasity)
                print("You now do",self.fistDamage,"damage with you fists")
                print("You now can hold",self.itemCapasity,"items")
            elif levelsUp > 1:
                print()
                print("You just went up",levelsUp,"levels! You are now level",self.level)
                print("You now have a max health of",self.healthCapasity)
                print("You now have a max spell capasity of",self.spellPointCapasity)
                print("You now do",self.fistDamage,"damage with you fists")
                print("You now can hold",self.itemCapasity,"items")
            else:
                print()
                print("You just went up a level! You are now level",self.level)
                print("You now have a max health of",self.healthCapasity)
                print("You now have a max spell capasity of",self.spellPointCapasity)
                print("You now do",self.fistDamage,"damage with you fists")
                print("You now can hold",self.itemCapasity,"items")
    def update(self):
        if self.health < self.healthCapasity:
            #gains more health the less you have, won't go above 50
            self.health = min(self.healthCapasity,self.health+int(40*((1/2)**((self.health)**(1/4)))))
        else:
            self.health = self.healthCapasity
    def addEx(self,amount):
        self.ex += amount
        self.updateLevel()
    def deleteItem(self,item):
        #deletes an item, ie doesn't drop it to the room
        #takes item object as input
        i = 0
        while i < len(self.items):
            if self.items[i] == item:
                self.items[i].loc = None
                self.items.pop(i)
            i+=1
    def display(self):
        clear()
        print("Item, the number you are carrying, damage/block chance/heal/points added, cost:")
        print()
        #using a dictionary lets me combine multiple identical items
        itemDict = {}
        #item dict format:
            #keys = names of items STRING
            #values = LIST with format
                #Val[0] = number carrying
                #Val[1] = Type of item
                #Val[2] = Damage
                #Val[3] = Cost
        for i in self.items:
            if self.weapon != None and i.name == self.weapon.name:
                useName = i.name+" (weapon)"
            elif self.armor != None and i.name == self.armor.name:
                useName = i.name+" (armor)"
            else:
                useName = i.name
            val = itemDict.get(useName,0)
            if val == 0:
                lst = []
                lst.append(1)
                lst.append(i.type)
                lst.append(i.damage)
                lst.append(i.cost)
                itemDict[useName] = lst
            else:
                itemDict[useName][0] += 1

        keys = list(itemDict.keys())
        vals = list(itemDict.values())
        weapons = []
        defense = []
        heal = []
        spell = []
        ex = []
        other = []
        for i in range(len(keys)):
            if vals[i][1] == "weapon":
                weapons.append(i)
            elif vals[i][1] == "defense":
                defense.append(i)
            elif vals[i][1] == "heal":
                heal.append(i)
            elif vals[i][1] == "spell":
                spell.append(i)
            elif vals[i][1] == "ex":
                ex.append(i)
            else:
                other.append(i)

        if len(weapons) > 0:
            print("Weapons:")
            for n in range(len(weapons)):
                i = weapons[n]
                print(str(keys[i])+",",vals[i][0],"," , vals[i][2],", ",vals[i][3])
            print()
        if len(defense) > 0:
            print("Defensive Items:")
            for n in range(len(defense)):
                i = defense[n]
                print(str(keys[i])+",",vals[i][0],","  , vals[i][2],", ",vals[i][3])
            print()
        if len(heal) > 0:
            print("Healing Items:")
            for n in range(len(heal)):
                i = heal[n]
                print(str(keys[i])+",",vals[i][0],","  , vals[i][2],", ",vals[i][3])
            print()
        if len(spell) > 0:
            print("Spell Items:")
            for n in range(len(spell)):
                i = spell[n]
                print(str(keys[i])+",",vals[i][0],","  , vals[i][2],", ",vals[i][3])
            print()
        if len(ex) > 0:
            print("Expirience Point Items:")
            for n in range(len(ex)):
                i = ex[n]
                print(str(keys[i])+",",vals[i][0],","  , vals[i][2],", ",vals[i][3])
            print()
        if len(other) > 0:
            print("Other Items:")
            for n in range(len(other)):
                i = other[n]
                print(str(keys[i])+",",vals[i][0],","  , vals[i][2],", ",vals[i][3])
                print()


        input("Press enter to continue...")
