import random
import math
import pr1testing
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):
        player1 = "player1"
        player2 = "player2"
        score1 = 0
        score2 = 0
        last = False
        while True:
            print()
            print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
            print('It is', player1 + "'s turn.")
            numDice = strat1(score1,score2,last)
            diceTotal = 0
            diceString = ""
            i = numDice
            while i > 0:
                d = roll()
                diceTotal += d
                diceString = diceString + " "  + str(d)
                i = i-1
            print("Dice rolled: ", diceString)
            print("Total for this turn: ", str(diceTotal))
            score1 += diceTotal
            if score1 > 100 or last:
                break
            if numDice == 0:
                last = True
            print()
            print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
            print('It is', player2 + "'s turn.")
            numDice = strat2(score2,score1,last)
            diceTotal = 0
            diceString = ""
            i = numDice
            while i > 0:
                d = roll()
                diceTotal += d
                diceString = diceString + " "  + str(d)
                i = i-1
            print("Dice rolled: ", diceString)
            print("Total for this turn: ", str(diceTotal))
            score2 += diceTotal
            if score2 > 100 or last:
                break
            if numDice == 0:
                last = True
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        if score1 > 100:
            print(player2 + " wins.")
            return 2
        elif score2 > 100:
            print(player1 + " wins.")
            return 1
        elif score1 > score2:
            print(player1 + " wins.")
            return 1
        elif score2 > score1:
            print(player2 + " wins.")
            return 2
        else:
            print("Tie.")
            return 3

def autoplay(strat1, strat2):
    player1 = "player1"
    player2 = "player2"
    score1 = 0
    score2 = 0
    last = False
    while True:
        numDice = strat1(score1,score2,last)
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        numDice = strat2(score2,score1,last)
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n):
    player1Wins=0
    player2Wins=0
    ties=0
    i=1
    win=0
    timesToRun = int(n/2)
    while i <= timesToRun:
        win = autoplay(strat1,strat2)
        if win == 1:
            player1Wins +=1
        elif win == 2:
            player2Wins +=1
        else:
            ties +=1
        i+=1
        win=0
    i=1
    win=0
    if n%2 != 0:
        timesToRun +=1
    while i <= timesToRun:
        win = autoplay(strat2,strat1)
        if win == 1:
            player2Wins +=1
        elif win == 2:
            player1Wins +=1
        else:
            ties +=1
        i+=1
        win=0
    print("Player 1 wins: " + str(player1Wins))
    print("Player 2 wins: " + str(player2Wins))
    print("Ties:          " + str(ties))
    return None

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
        return 12

def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif 51 <= myscore and myscore <=80:
        return 10
    elif 80 < myscore:
        return 0

def improve(strat1):
    def strat2(myscore,theirscore,last):
        if myscore == 100:
            return 0
        else:
            return strat1(myscore,theirscore,last)
    return strat2

def myStrategy(myscore,theirscore,last):
# general idea for the strategy is that it makes a bunch of guesses about how many dice and then checks them for the best
#originally unintended benefit is that when there's a small delta left, the rolls will all be either 0 or 1 which then checks each of those mulitple times
    import random
    def roll(dice):
    #will use this function later to approximate the rolls
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[] #keeps track of number of dice from each run through
    V =[] #stores the values from each of the dice rolls
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    runs=2
    #want to be more/less aggressive depending on the state of the game
    #diving delta by a higher number (closer to 5) will give a lower number of dice
    if myscore<theirscore and last:
        #wider variety of roll options if this is the last roll
        options[0] = delta//2.5
        options[1] = delta//3
        options[2] = delta//3.5
        options[3] = delta//3.75
        options[4] = delta//4
    elif myscore > theirscore:
        # more conservative rolls if winning
        options[0] = delta//3.15
        options[1] = delta//3.3
        options[2] = delta//3.45
        options[3] = delta//3.6
        options[4] = delta//3.75
    else:
        #this case means either scores are equal, or losing and not last. Moderatly aggressive.
        options[0] = delta//3
        options[1] = delta//3.25
        options[2] = delta//3.4
        options[3] = delta//3.75
        options[4] = delta//4
    while i < runs:
    #loop this part twice so it calculates the rolls/best number of dice twice
    #options is just a list with 5 numbers of dice, values actually gets the total of the dice
        values = [roll(x) + myscore for x in options]
        end = True
        if min(values) > 100:
            #returns 0 since all possible rolls result in going over 100
            D.append(0)
            V.append(0)
        elif min(options) == max(options):
            #not greater than 100, but all rolls give the same output so don't need to find the max
            D.append(options[0])
            V.append(values[0])
        else:
            # this is the actual calculation part
            while end:
                if max(values) >100:
                    #if the highest value is over 100, not a good roll and don't want it
                    #remove this value from the list and try again until it isn't over 100
                    #don't need to worry about all elements being removed(if all over 100) because accounted for that earlier with the if statements
                    values.remove(max(values))
                else:
                    #if the highest value isn't over 100, that's the number we want
                    #save it to the list so we can compute later what the average of the 2(+) attempts is
                    index=values.index(max(values))
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    #find the average result score and number of dice
    val = sum(V)//runs
    dice = sum(D)//runs
    if  abs(val - myscore)<1 and last:
        #if nothing is added and it's the last roll, probably want to roll anyway but check if losing first
        if myscore < theirscore:
            #if last roll, usually max(int(delta/3)) is going to be 0, still want to roll and try
            dice = max(delta//3,1)
        else:
            #if tied or winning and last roll, don't mess it up
            dice = 0
    elif myscore < theirscore and last:
        dice = max(delta//3,1,dice)
    return dice
