from item import Item
import os
import random
import copy
from itemLists import itemList


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Merchant:
    def __init__(self):
        self.name = "Merchant"
        self.items = []
        self.addItem()
    def listItems(self):
        print("The items available for sale are:")
        print()
        for i in self.items:
            print(i.name,"costs",i.cost)
    def addItem(self):
        #adds items by picking randomly from the list of items available
        #also checks that item is not currently on sale
        while len(self.items) < 3:
            done = False
            while not done:
                index = random.randint(0,len(itemList)-1)
                if not self.checkForItem(itemList[index].name):
                    self.items.append(copy.deepcopy(itemList[index]))
                    done = True
    def deleteItem(self,item):
        #removes item from merchant's list of items
        self.items.pop(self.items.index(item))
    def sell(self,item,player):
        #sells an item to the player
        useItem = self.items[self.findItem(item)]
        if player.currency >= useItem.cost:
            player.buyItem(useItem)
            self.deleteItem(useItem)
            print("You have successfully purchased: ", useItem.name)
        else:
            print("Insufficient funds to purchase")
            print("This item costs",useItem.cost,"to purchase.")
            print("You only have",player.currency,"currently.")
    def buy(self,item,buyPrice,player):
        #buys an item from the player
        player.sellItem(item,buyPrice)
    def checkForItem(self,item):
        #checks if the item (given by name) is for sale
        for i in self.items:
            if item.lower() == i.name.lower():
                return True
        return False
    def findItem(self,item):
        #finds where the item (specified by name) is in the list of items for sale
        for i in range(3):
            if item == self.items[i].name.lower():
                return i
    def buyTransaction(self,item,player):
        #deals with selling an item to the merchant
        useItem = player.findItemByName(item)
        merchantPrice = useItem.cost*(0.75)
        print()
        print("This",useItem.name,"has a value of",str(useItem.cost)+".\nThe merchant will pay",merchantPrice,"for it.")
        choice = input("Would you like to sell to the merchant? (yes/y or no/n) ")
        if choice.lower() == "yes" or choice.lower() == "y":
            self.buy(useItem,merchantPrice,player)
            print("You have successfully sold",useItem.name,"to the merchant for",str(merchantPrice)+". Thank you for doing buisness with us!")
        elif choice.lower() == "no" or choice.lower() == "n":
            print("You have elected not to sell anything.")
        else:
            print("That item is not for sale, please try again.")
