from room import Room
from player import Player
from item import Item
from monster import Monster
from merchant import Merchant
from merchantInteract import merchantUI
from fightInteract import fightUI
import os
import updater
import copy
from itemLists import itemList
from itemLists import monsterList
import random
from itemLists import specialList
from itemLists import roomList
player = Player()
merchant = Merchant()
#main file for running game, this is what should be opened to play


#some options for rooms, all fit the necessary condition of reflexivity
directions = ["NorthWest","NorthEast","North","East","West","South","SouthWest","SouthEast"]
#shortDirs = ["North","East","West","South"]
#directions = ["NorthWest","North","East","West","South","SouthEast"]


#can ignore the first 4 functions, just for testing the room generation
def findLoops(roomList):
    #finds how many loops of non-intersecting rooms exist
    loops = []
    for n in roomList:
        lst = crawlerLoud(roomList,n)
        if sorted(lst) not in loops:
            loops.append(sorted(lst))
    return [len(loops),loops]


def clearExits(roomList):
    #clears the exits
    for n in roomList:
        n.exits = []

def crawlerLoud(roomList,startRoom):
    #spends 10 seconds going through and randomly walking around rooms
    #since rooms are being generated randomly, want to make sure all rooms are accessible
    outLst = []
    import time
    init = time.time()
    loc = startRoom
    while time.time() - init < .25:
        if loc.desc not in outLst:
            #if this is a new room, add it to the list
            outLst.append(loc.desc)
        loc = loc.getDestination(loc.exits[random.randint(0,len(loc.exits)-1)][0])
    return outLst

def crawlerQuiet(roomList):
    #spends 10 seconds going through and randomly walking around rooms
    #since rooms are being generated randomly, want to make sure all rooms are accessible
    outLst = []
    import time
    init = time.time()
    loc = roomList[0]
    while time.time() - init < .25:
        if loc.desc not in outLst:
            #if this is a new room, add it to the list
            outLst.append(loc.desc)
        loc = loc.getDestination(loc.exits[random.randint(0,len(loc.exits)-1)][0])
    if len(outLst) == len(roomList):
        #if all rooms are accounted for, return true
        return True
    else:
        #if rooms not accounted for, print which ones those are
        for n in roomList:
            if n.desc not in outLst:
                print(n.desc)

def createConnections(lst,useRoom,num,directions):
    #creates the connections for a single room
    free = 0
    for i in lst:
        if len(i.exits) < num:
            free += num-len(i.exits)
    while free > (num - len(useRoom.exits)) and len(useRoom.exits) < num:
        toConnect = lst[random.randint(0,len(lst)-1)]
        while useRoom.checkForConnection(toConnect.index) or len(toConnect.exits) >= num:
            #makes sure rooms aren't already connected
            #and that room being connected too isn't too full of connections
            toConnect = lst[random.randint(0,len(lst)-1)]
        dir = random.randint(0,len(directions)-1)
        while useRoom.checkForDir(directions[dir]) or toConnect.checkForDir(directions[-(dir+1)]):
            #checks the directions being added so they'll work
            dir = random.randint(0,len(directions)-1)
        useRoom.connectRooms(directions[dir],toConnect,directions[-(dir + 1)])
        free -= 1

def createWorld(roomList,dirs,num):
    #creates the world, works for a generic length list of rooms so this scales
    for i in range(len(roomList)):
        createConnections(roomList[:i]+roomList[i+1:],roomList[i],num,dirs)
    player.location = roomList[0]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("Command options while walking in rooms are:")
    print()
    print("go <direction> -- moves you in the given direction")
    print("inventory or i -- opens your inventory")
    print("self or s -- displays various information about the self")
    print("pickup <item>  or p <item> -- picks up the item")
    print("attack <monster> or a <monster> -- attacks the monster")
    print("exit -- quits the game")
    print("wait or w -- allows time to pass without any action occuring")
    print("drop <item> -- discards a specified item from the inventory into the current room")
    print("view <item> or v <item> -- takes a closer look at an item and displays useful information")
    print("set weapon <item> -- equips the specified weapon")
    print("set armor <item> -- equips the specified item as armor")
    print("use <item> -- uses a consumable (heal,spell, or ex item)")
    print("display or dis -- shows expanded information about all of the items in your inventory")
    print("observe <monster> or o <monster> -- lists the monsters stats")
    print("tips or t -- shows hints about the game, try it out to make sure you're taking advantage of everything!")
    print()
    input("Press enter to continue...")

def printStart(specialList):
    clear()
    print("You work in a restaurant that has been overtaken by monsters!")
    print("You have discovered that the only way to defeat the monsters is by collecting all",len(specialList),"special items")
    print("The special items will appear randomly throughout the restaurant, but beware the monsters may try to kill you!")
    print("The special items are:")
    for i in specialList:
        print(i.name)
    print()
    print("Use items as weapons and armor to make yourself stronger in battle")
    print("You can also use spells to deal large amounts of damage")
    print("Level up by getting enough experience points to increase your health and other stats")
    print("Use potions to heal your health, gain experience points, and refill your spell points")
    print()
    print("When you defeat monsters they will drop currency which can be used to buy items from the merchant")
    print("You can also gain currency by selling items to the merchant")
    print()
    print("If you're lost, try typing 'help'")
    input("Press enter to start the game...")

def randomness(lst,chance):
    #works for placing either monsters or items randomly
    if random.random() < chance:
        itemIndex = random.randint(0,len(lst)-1)
        return lst[itemIndex]

def convertDir(input):
    #allows for abbreviations in directions
    #specifically for NW and SE, annoying to write the whole word
    #also accounts for capitalization errors now
    #only works on directions = [northwest,north,east,west,south,southeast]
        #ie, northeast and southwest don't exist for this function
    input = input.lower()
    if input == '':
        return None
    elif input[0] == "n":
        if input == "n" or input == "north":
            return "North"
        elif input == "nw" or input == "northwest":
            return "NorthWest"
        elif input == "ne" or input == "northeast":
            return "NorthEast"
        else:
            return None
    elif input[0] == "s":
        if input == "s" or input == "south":
            return "South"
        elif input == "se" or input == "southeast":
            return "SouthEast"
        elif input == "sw" or input == "southwest":
            return "SouthWest"
        else:
            return None
    elif input == "west" or input == "w":
        return "West"
    elif input == "east" or input == "e":
        return "East"
    else:
        return None

def printHints():
    clear()
    print("Capitalization doesn't matter when giving inputs, either capitalize or don't!")
    print("Walking, fighting, and the merchant's shop all have different help screens, try them out!")
    print("You can enter the merchant's shop at any time, try it out!")
    print("You can abbreviate directions instead of writing the whole word out! (Try 'NW' instead of 'NorthWest')")
    print("If you're low on health, try looking for healing items")
    print()
    input("Press enter to continue...")

#how likely random drops are
itemChance = .25
monsterChance = .3
monsterFightChance = .1
specialItemChance = .1
specialFightChance = .1

createWorld(roomList,directions,3)
printStart(specialList)
playing = True
while playing and player.alive:
    #randomly put a max of 1 monster and 1 item in the room that the player is currently in
    #discourages player to wait infinitely since monsters will show up
    if len(player.location.monsters) < 3:
        monsterPlace = copy.deepcopy(randomness(monsterList,monsterChance))
        if monsterPlace is not None:
            if player.location.checkForMonster(monsterPlace.name):
                while player.location.checkForMonster(monsterPlace.name):
                    monsterPlace = monsterList[random.randint(0,len(monsterList)-1)]
            monsterPlace.putInRoom(player.location)

    if len(player.location.items) < 1:
        itemPlace = copy.deepcopy(randomness(itemList,itemChance))
        if itemPlace is not None:
            while player.location.checkForItem(itemPlace.name):
                #runs as long as the item being added to the room already exists in the room
                #ie, makes sure a unique item is being added
                itemPlace = itemList[random.randint(0,len(itemList) -1)]
            while len(player.items)>1 and player.items[-1].name == itemPlace.name:
                #makes sure that the player doesn't get the samne item twice in a row
                itemPlace = itemList[random.randint(0,len(itemList) -1)]
            itemPlace.putInRoom(player.location)

    if len(player.location.monsters) > 0:
        #if there are monsters in the room, randomly might make you fight a monster
        if random.random() < monsterFightChance:
            clear()
            print("A monster has decided to attack you!")
            input("Press enter to continue to fight the monster  ")
            fightUI(player,player.location.monsters[random.randint(0,len(player.location.monsters)-1)])

    if len(specialList) > 1:
        #will randomly place the special items in rooms
        #places two items randomly into rooms, but forces you to fight for the last one
        if random.random() < specialItemChance:
            specialList[random.randint(0,len(specialList)-1)].putInRoom(player.location)
    elif len(specialList) == 1:
        #once you have two of the three special items, will eventually make you fight for the last one
        #if you win the fight, the last item is added to your inventory and you win
        #if you lose, the game is over
        #the monster is too fast, so you can't escape from it
        if random.random() < specialFightChance:
            m=Monster("the chef",65,25,100,player.location)
            print("The final monster has appeared. Defeat the chef and you will recieve the last of the three special ingredients")
            print("You cannot escape the chef, win or die")
            input("Press enter to continue to fight the chef...")
            fightUI(player,m)
            if player.alive:
                specialList[0].putInRoom(player.location)
                player.pickup(specialList[0])

    if player.alive:
        printSituation()
        commandSuccess = False
        timePasses = False
    else:
        commandSuccess = True
        timePasses = False

    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if command == '':
            print("Not a valid command")
            commandSuccess = False
        elif commandWords[0].lower() == "go":   #cannot handle multi-word directions
            dir = convertDir(command[3:])
            if dir is not None:
                if player.goDirection(dir):
                    timePasses = True
                else:
                    print("Invalid direction, please try again")
                    commandSuccess = False
            else:
                print("Invalid direction, please try again")
                commandSuccess = False
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                if target.type == "win":
                    for i in specialList:
                        if i.name == target.name:
                            specialList.pop(specialList.index(i))
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == 'p':
            targetName = command[2:]
            target = player.location.getItemByName(targetName)
            if target != False:
                if target.type == "win":
                    for i in specialList:
                        if i.name == target.name:
                            specialList.pop(specialList.index(i))
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "inventory" or commandWords[0].lower() == 'i':
            player.showInventory()
        elif commandWords[0].lower() == "help" or commandWords[0].lower() == 'h':
            showHelp()
        elif commandWords[0].lower() == "self" or commandWords[0].lower() == "s":
            player.showStatus()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "tips" or commandWords[0].lower() == "t":
            printHints()
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            #first need to check that monster is in the room, if so fight, if not don't fight
            target = player.location.getMonsterByName(targetName)
            if target != False:
                fightUI(player,target)
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == 'a':
            targetName = command[2:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                fightUI(player,target)
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == "observe":
            targetName = command[8:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                target.inspect()
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == "o":
            targetName = command[2:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                target.inspect()
            else:
                print("No such monster.")
                commandSuccess = False
        elif commandWords[0].lower() == 'merchant' or commandWords[0].lower() == 'm':
            merchantUI(player,merchant)
        elif commandWords[0].lower() == "wait" or commandWords[0].lower() == "w":
            #lets time pass with nothing else occuring
            #player regens health over time, so this can be helpful
            timePasses = True
        elif commandWords[0].lower() == "drop":
            #drop an item
            if player.checkForItem(command[5:].lower()):
                player.discardItem(command[5:].lower())
                print("Successfully dropped",command[5:])
                input("Press enter to continue...")
            else:
                print("You are not carrying that item")
                commandSuccess = False
        elif commandWords[0].lower() == "view":
            #inspect an item in your inventory or the merchant's inventory
            #displays some stats and info about it
            if player.checkForItem(command[5:].lower()):
                player.findItemByName(command[5:].lower()).describe()
            elif player.location.checkForItem(command[5:].lower()):
                player.location.getItemByName(command[5:].lower()).describe()
            else:
                print("There is no such item")
                commandSuccess = False
        elif commandWords[0].lower() == "v":
            if player.checkForItem(command[2:].lower()):
                player.findItemByName(command[2:].lower()).describe()
            elif player.location.checkForItem(command[2:].lower()):
                player.location.getItemByName(command[2:].lower()).describe()
            else:
                print("There is no such item")
                commandSuccess = False
        elif commandWords[0].lower() == "set":
            #equip weapons and armor easily
            if commandWords[1].lower() == "weapon":
                if player.checkForItem(command[11:]):
                    player.setWeapon(command[11:])
                else:
                    print("There is no such item")
                    commandSuccess = False
            elif commandWords[1].lower() == "armor":
                if player.checkForItem(command[10:]):
                    player.setArmor(command[10:])
                else:
                    print("There is no such item")
                    commandSuccess = False
            else:
                print("Not a valid command")
                commandSuccess = False
        elif commandWords[0].lower() == "use":
            #healing command, use a heal item
            if player.checkForItem(command[4:].lower()):
                item = player.findItemByName(command[4:].lower())
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
                    print("You added",player.spellPoints - oldSpellPoints,"spell points")
                    print("You had",oldSpellPoints,"spell points and now have,",player.spellPoints)
                    input("Press enter to continue...")
                elif item.type == "ex":
                    player.deleteItem(item)
                    oldEx = player.ex
                    player.addEx(item.damage)
                    print("You added",item.damage,"experience points")
                    print("You had",oldEx,"experience points and now have",player.ex)
                    input("Press enter to continue...")
                else:
                    print("Wrong item type, can only heal with heal items or add spell points with spell items")
                    commandSuccess = False
            else:
                print("No such item")
                commandSuccess = False
        elif commandWords[0].lower() == "display" or commandWords[0].lower() == "dis":
            #basically view, but for every item in the inventory so you don't have to view multiple times to compare stats
            player.display()
        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()
        player.update()
