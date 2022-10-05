from player import Player
from monster import Monster
from item import Item
import random
import os
#how the player fights, new/specified version of the main file

from room import Room

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showHelp(player):
    clear()
    print("Command options during a fight are:")
    print()
    print("attack -- attacks the monster")
    print("defend -- boosts your armor by "+str(player.focusBenefit)+"% for the next",player.focusLength,"turns")
    print("flee -- attempts to run away from the monster")
    print("help or h -- displays this screen")
    print("self -- displays various information about the self")
    print("stats -- displays stats about you and the monster")
    print("spell info -- displays information on using spells")
    print("spell <size> -- attacks with the specified spell size, if you have enough spell points")
    print("view <item> or v <item> -- takes a closer look at an item and displays useful information")
    print("drop <item> -- discards a specified item from the inventory into the current room")
    print("inventory or i -- opens your inventory")
    print("set weapon <item> -- equips the specified weapon")
    print("set armor <item> -- equips the specified item as armor")
    print("use <item> -- uses a consumable (heal,spell, or ex item)")
    print("display or dis -- shows expanded information about all of the items in your inventory")
    print("exit -- quits the game")
    print()
    input("Press enter to continue...")

def printLastTurn(player,monster,damage,playerChoice):
    #can't give damage = none
    #prints the last turn/what was done by the last character to move
    #really just reformats the data it's given to print it well
    #player choice is explained below, basically just keeps track of what the player did on the last turn
        #one exception is 0, which means monster went
    clear()
    if playerChoice == 1:
        print("Last turn, you attacked the monster and did",damage,"damage")
    elif playerChoice == 2:
        print("Last turn, you attempted to flee but were caught by the monster")
    elif playerChoice == 3:
        print("Last turn, you fortified your armor")
        print("For the next",player.focusLength,"turns your armor will be boosted by "+str(player.focusBenefit)+"%")
    elif playerChoice == 4:
        print("Last turn, you used a spell which did",damage,"damage")
    elif playerChoice == 5:
        print("Last turn, you healed yourself by",damage,"health")
    elif playerChoice == 6:
        print("Last turn, you added",damage,"spell points")
    elif playerChoice == 7:
        print("Last turn, you added",damage,"ex points")
    elif playerChoice == 0:
        if damage == 0:
            print("Last turn, the monster attempted to attack but your armor blocked it")
        else:
            print("Last turn, the monster attacked and did",damage,"damage")
    print()
    print("You have",player.health,"health left")
    print("The monster has",monster.health,"health left")
    input("Press enter to continue...")
    print()

def printStats(player,monster,focusRemainder):
    clear()
    if focusRemainder is None:
        #this is for the first time it prints, can't be anything other than none
        #lets me re-use this function for the first time through
        print("You are fighting",monster.name)
        print()
    print("You have",player.health,"health left")
    print("The monster has",monster.health,"health left")
    print()
    print("The monster has a "+str(monster.speed)+"% chance of stopping you from fleeing")
    print()
    if player.weapon is not None:
        #this is done more elegantly in the full function
        #makes sure that player.weapon.name won't give an error
        print("You are attacking with",player.weapon.name)
        print("You do",player.weapon.damage,"damage per attack")
    else:
        print("You are attacking with your fists")
        print("You do",player.fistDamage,"damage per attack")
    print("The monster does",monster.damage,"damage per attack")
    print()
    if player.armor is not None:
        #same as above for weapon, but for armor
        print("You are wearing",player.armor.name,"armor")
        if focusRemainder == 0 or focusRemainder is None:
            #no boost remaining is a more complicated case than boost
            print("Your armor has a "+str(player.armor.damage)+"% chance of blocking an attack")
            print("By fortifying you can increase your armor's chance of working by "+str(player.focusBenefit)+"% for",player.focusLength,"turns")
            print("This would give you a "+str(player.armor.damage + player.focusBenefit)+"% chance of blocking an attack")
        else:
            print("Your armor will be boosted for the next",focusRemainder,"turns")
            print("This means your armor has a "+str(player.armor.damage + player.focusBenefit)+"% chance of blocking an attack")
    input("Press enter to continue...")
    print()

def printSpellInfo(player,monster):
    #prints info on how the spell system works
    #not as standardized as weapons, wanted to give info for that
    clear()
    print("There are three types of spells, each does a different amount of damage and uses a different amount of spell points")
    print("If you do not have enough spell points for a spell, you cannot use it")
    print()
    print("Your small spell costs",player.smallSpellCost,"and removes "+str(player.smallSpellDamage)+"% of the opponent's health")
    print("If you were to use this spell right now, it would do",int(monster.health*(player.smallSpellDamage/100)),"damage")
    print()
    print("Your medium spell costs",player.medSpellCost,"and removes "+str(player.medSpellDamage)+"% of the opponent's health")
    print("If you were to use this spell right now, it would do",int(monster.health*(player.medSpellDamage/100)),"damage")
    print()
    print("Your large spell costs",player.largeSpellCost,"and removes "+str(player.largeSpellDamage)+"% of the opponent's health")
    print("If you were to use this spell right now, it would do",int(monster.health*(player.largeSpellDamage/100)),"damage")
    print()
    print()
    print("You currently have",player.spellPoints,"spell points left")
    print()
    input("Press enter to continue...")

def fightUI(player,monster):
    turn = random.randint(0,1)
    # turn of 0 means monster attacks, 1 means player attacks
    #this way it's randomly decided

    battle = True

    #standardize armor so that if you this doesn't have to be accounted for later
    #only have to do once, and good for the rest of the fight
    if player.armor is not None:
        playerArmorRating = player.armor.damage
    else:
        playerArmorRating = 0
    tempArmorRating = playerArmorRating
    focusBenefit = player.focusBenefit
    focusRemainder = 0

    #standardize weapon damage, if weapon exists
    #avoids errors if player doesn't have weapon equiped
    if player.weapon is not None:
        playerWeaponDamage = player.weapon.damage
    else:
        playerWeaponDamage = player.fistDamage

    monsterWeaponDamage = monster.damage
    monsterSpeed = monster.speed

    damage = None

    while battle:
        #turn variable says which player's turn it is
            #turn changes at the end of each evaluation of this loop
            #so if turn (at this point in the loop) says it's the players turn, it was just the monster's turn
            #0 = monster's turn
            #1 = Player's turn
        #Playeraction variable keeps track of what the player did on the last turn
            #mostly going to use for printing the last turn
            #0 means it was the monster's turn
            #1 means the player attacked
            #2 means the player attempted (unsuccessfully) to flee
            #3 means the player forified
            #4 means the player used a spell
            #5 means the player healed
            #6 means the player added spell points
            #7 means the player added EX points
        clear()
        if damage is not None:
            #only doesn't display on the first turn
            printLastTurn(player,monster,damage,playerChoice)
        else:
            #only does print on the first turn
            print("You are fighting",monster.name)
            print()
            printStats(player,monster,None)
        if turn == 0:
            #monster's turn
            attack = random.randint(0,100)
            if attack < max(playerArmorRating,tempArmorRating):
                #account for the armor/boost systems
                #this is how the player "blocks" attacks
                damage = 0
            else:
                damage = monsterWeaponDamage
            #allows focusRemainder to be updated every time without caring about if it was just used or not
            focusRemainder = max(0,focusRemainder-1)
            if focusRemainder == 0:
                #reset tempArmor, if applicable
                tempArmorRating = playerArmorRating

            #get ready to print info and next turn
            playerChoice = 0
            turn = 1

        else:

            damage = 0
            timePasses = False
            #player options more complicated, sometimes time doesn't pass

            while timePasses is False:
                command = input("What now? ")
                command = command.lower()
                #makes all input lowercase, no string errors

                if command == '':
                    print("Not a valid command")
                elif command == "attack" or command == "a":
                    damage = playerWeaponDamage
                    playerChoice = 1
                    timePasses = True
                elif command == "flee":
                    #randomness of if you can escape or not, tied to monster speed atribute
                    runAttempt = random.randint(0,100)
                    if runAttempt > monsterSpeed:
                        battle = False
                        playerChoice = None
                        print("You have successfully escaped the monster")
                        input("Press enter to continue...")
                    else:
                        playerChoice = 2
                    timePasses = True
                elif command == "help" or command == "h":
                    showHelp(player)
                elif command == "defend":
                    if player.armor is None:
                        #can't fortify/defend if you aren't wearing any armor
                        print("You are not wearing armor")
                    else:
                        #adds benefit to armor for however many turns
                        tempArmorRating = playerArmorRating + focusBenefit
                        focusRemainder = player.focusLength
                        playerChoice = 3
                        timePasses = True
                elif command == "stats":
                    printStats(player,monster,focusRemainder)
                elif command == "self":
                    player.showStatus()
                elif command[:5] == "spell":
                    #if doing anything with spells, starts with 'spell'
                    if command[6:] == "info":
                        printSpellInfo(player,monster)
                    elif command[6:] == "small":
                        #small/med/large bascially all the same, just different damages/costs
                        #sees if the player has enough spell points, if so attacks
                        if player.spellPoints >= player.smallSpellCost:
                            damage = int(monster.health*(player.smallSpellDamage/100))
                            player.spellPoints -= player.smallSpellCost
                            timePasses = True
                            playerChoice = 4
                        else:
                            print("You do not have enough spell points for that spell")
                    elif command[6:] == "medium" or command[6:] == "med":
                        if player.spellPoints >= player.medSpellCost:
                            damage = int(monster.health*(player.medSpellDamage/100))
                            player.spellPoints -= player.medSpellCost
                            timePasses = True
                            playerChoice = 4
                        else:
                            print("You do not have enough spell points for that spell")
                    elif command[6:] == "large":
                        if player.spellPoints >= player.largeSpellCost:
                            damage = int(monster.health*(player.largeSpellDamage/100))
                            player.spellPoints -= player.largeSpellCost
                            timePasses = True
                            playerChoice = 4
                        else:
                            print("You do not have enough spell points for that spell")
                    else:
                        print("Invalid input for spell")
                elif command[:4] == "view":
                    #lets the player inspect items mid-battle
                    if player.checkForItem(command[5:]):
                        player.findItemByName(command[5:]).describe()
                    else:
                        print("There is no such item")
                elif command[:1] == "v":
                    if player.checkForItem(command[2:]):
                        player.findItemByName(command[2:]).describe()
                    else:
                        print("There is no such item")
                elif command[:4] == "drop":
                    #not sure why this would be super helpful, but the player can drop items mid-battle
                    if player.checkForItem(command[5:]):
                        player.discardItem(command[5:])
                    else:
                        print("You are not carrying that item")
                elif command[:9] == "inventory" or command[:1] == 'i':
                    player.showInventory()
                elif command == "exit":
                    battle = False
                    timePasses = True
                    player.alive = False
                elif command[:3] == "set":
                    #lets the player equip weapons/armor if they have the items
                    if command[4:10] == "weapon":
                        if player.checkForItem(command[11:]):
                            player.setWeapon(command[11:])
                            playerWeaponDamage = player.findItemByName(command[11:]).damage
                        else:
                            print("There is no such item")
                    elif command[4:9] == "armor":
                        if player.checkForItem(command[10:]):
                            player.setArmor(command[10:])
                            playerArmorRating = player.findItemByName(command[10:]).damage
                        else:
                            print("There is no such item")
                    else:
                        print("Not a valid command")
                elif command[:3].lower() == "use":
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
                            timePasses = True
                            damage = item.damage
                            playerChoice = 5
                        elif item.type == "spell":
                            player.deleteItem(item)
                            oldSpellPoints = player.spellPoints
                            player.addSpellPoints(item.damage)
                            print("You added",item.damage,"spell points")
                            print("You had",oldSpellPoints,"spell points and now have,",player.spellPoints)
                            input("Press enter to continue...")
                            playerChoice = 6
                            damage = item.damage
                            timePasses = True
                        elif item.type == "ex":
                            player.deleteItem(item)
                            oldEx = player.ex
                            player.addEx(item.damage)
                            print("You added",item.damage,"expirience points")
                            print("You had",oldEx,"expirience points and now have",player.ex)
                            input("Press enter to continue...")
                            playerChoice = 7
                            damage = item.damage
                            timePasses = True
                        else:
                            print("Wrong item type, can only heal with heal items or add spell points with spell items")
                    else:
                        print("No such item")
                elif command.lower() == "display" or command.lower() == "dis":
                    #displays helpful stats about all items in inventory to compare them all in one place
                    player.display()
                else:
                    print("Not a valid command")

                #reset to the monster's turn
                turn = 0


        if turn == 0:
            #turn = 0 means monster's turn NEXT, important distinction to note at the end of the run
            if playerChoice == 1:
                monster.health -= damage
        else:
            player.health -= damage

        if player.health < 1 or monster.health < 1:
            #one of the fighters was killed
            if monster.health < 1:
                monster.die()
                curr = (monster.damage+monster.maxHealth)//random.randint(1,5)
                player.addCurrency(curr)
                ex = curr//2
                print("The",monster.name,"was defeated")
                print("You gained",curr,"currency for defeating the",monster.name)
                print("You gained",ex,"expirience for defeating the",monster.name)
                player.addEx(ex)
                input("Press enter to continue...")
                battle = False
            else:
                printLastTurn(player,monster,damage,playerChoice)
                print("You lose")
                input("Press enter to continue...")
                player.alive = False
                battle = False
