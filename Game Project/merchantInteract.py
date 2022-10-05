import os
from player import Player
from merchant import Merchant
from item import Item
#in essence, the merchant's shop
#this is where/how the playr interacts with the merchant


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showHelp():
    clear()
    print("Command options in the merchant's shop are:")
    print()
    print("help or h -- displays this screen")
    print("leave -- leaves the merchant")
    print("inventory or i -- opens your inventory")
    print("self or s -- displays various information about the self")
    print("browse -- displays the items for sale and their price")
    print("buy <item> or b <item> -- buys a specified item")
    print("sell <item> -- sells a specified item")
    print("view <item> or v <item> -- takes a closer look at an item and displays useful information")
    print("drop <item> -- discards a specified item from the inventory into the current room")
    print("inventory or i -- opens your inventory")
    print("set weapon <item> -- equips the specified weapon")
    print("set armor <item> -- equips the specified item as armor")
    print("use <item> -- uses a consumable (heal,spell, or ex item)")
    print("display or dis -- shows expanded information about all of the items in your inventory")
    print()
    input("Press enter to continue...")



def merchantUI(player,merchant):
    buying = True
    clear()
    print("Welcome to the Merchant! You can buy or sell items here in exchange for currency. \nThe Merchant will always have three items for sale which you can purchase. \nOnce you obtain enough currency, you will also be able to purchase passage off of the planet.")
    while buying:
        merchant.addItem()
        print("You are in the Merchant's shop.\n \n")
        choice = input("What would you like to do? ")
        clear()
        choiceWords = choice.split()
        if choice == '':
            print("Not a valid command")
        elif choiceWords[0].lower() == "buy":
            if len(player.items) < player.itemCapasity:
                if merchant.checkForItem(choice[4:].lower()):
                    merchant.sell(choice[4:].lower(),player)
                else:
                    print("Invalid item name, please try again")
            else:
                print("Insufficient space to pickup items")
        elif choiceWords[0].lower() == "b":
            if merchant.checkForItem(choiceWords[1].lower()):
                merchant.sell(choiceWords[1].lower(),player)
            else:
                print("Invalid item name, please try again")
        elif choiceWords[0].lower() == "inventory" or choiceWords[0].lower() == 'i':
            player.showInventory()
            clear()
        elif choiceWords[0].lower() == "help" or choiceWords[0].lower() == 'h':
            showHelp()
        elif choiceWords[0].lower() == "self" or choiceWords[0].lower() == "s":
            player.showStatus()
        elif choiceWords[0].lower() == "leave":
            buying = False
        elif choiceWords[0].lower() == "browse":
            merchant.listItems()
        elif choiceWords[0].lower() == "sell":
            if player.checkForItem(choice[5:].lower()):
                if player.checkWeaponArmor(choice[5:]):
                    print("You must unequip",choice[5:],"before you can sell it")
                else:
                    merchant.buyTransaction(choice[5:].lower(),player)
            else:
                print("You do not have that item in your inventory, please try again.")
        elif choice[:4] == "view":
            #inspect items for sale or in your inventory
            if player.checkForItem(choice[5:].lower()):
                player.findItemByName(choice[5:].lower()).describe()
            elif merchant.checkForItem(choice[5:].lower()):
                merchant.items[merchant.findItem(choice[5:].lower())].describe()
            else:
                print("There is no such item")
        elif choice[:1] == "v":
            if player.checkForItem(choice[2:].lower()):
                player.findItemByName(choice[2:].lower()).describe()
            elif merchant.checkForItem(choice[2:].lower()):
                merchant.items[merchant.findItem(choice[2:].lower())].describe()
            else:
                print("There is no such item")
        elif choice[:4] == "drop":
            if player.checkForItem(choice[5:]):
                player.discardItem(choice[5:])
                print("Successfully dropped",choice[5:])
                input("Press enter to continue...")
            else:
                print("You are not carrying that item")
        elif choice[:9] == "inventory" or choice[:1] == 'i':
            player.showInventory()
        elif choice[:3] == "set":
            #can equip weapons or armor right in the merchant's shop
            if choice[4:10] == "weapon":
                if player.checkForItem(choice[11:]):
                    player.setWeapon(choice[11:])
                else:
                    print("There is no such item")
            elif choice[4:9] == "armor":
                if player.checkForItem(choice[10:]):
                    player.setArmor(choice[10:])
                else:
                    print("There is no such item")
            else:
                print("Not a valid command")
        elif choice[:3].lower() == "use":
            #healing command, use a heal item
            if player.checkForItem(choice[4:].lower()):
                item = player.findItemByName(choice[4:].lower())
                if item.type == "heal":
                    player.deleteItem(item)
                    oldHealth = player.health
                    player.addHealth(item.damage)
                    print("You healed for",player.health - oldHealth,"health")
                    print("You were at",oldHealth,"health and are now at",player.health)
                    input("Press enter to continue...")
                elif item.type == "spell":
                    player.deleteItem(item)
                    oldSpellPoints = player.spellPoints
                    player.addSpellPoints(item.damage)
                    print("You added",item.damage,"spell points")
                    print("You had",oldSpellPoints,"spell points and now have,",player.spellPoints)
                    input("Press enter to continue...")
                elif item.type == "ex":
                    player.deleteItem(item)
                    oldEx = player.ex
                    player.addEx(item.damage)
                    print("You added",item.damage,"expirience points")
                    print("You had",oldEx,"expirience points and now have",player.ex)
                    input("Press enter to continue...")
                else:
                    print("Wrong item type, can only heal with heal items or add spell points with spell items")
            else:
                print("No such item")
        elif choice.lower() == "display" or choice.lower() == "dis":
            #displays stats about all the items in inventory
            player.display()
        else:
            print("Not a valid command")
        print("\n")
