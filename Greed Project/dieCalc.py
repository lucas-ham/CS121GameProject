def  dieCalc(min,max,dice):
    #takes as input minimum and maximum values to choose an integer from
    # also takes a number of dice to roll
    # runs the specified number of times and outputs the average value outputted by the randint function
    import random
    total=0
    i=0
    while i < dice:
        total += random.randint(min,max)
        i+=1
    return total/dice

def runDies(min,max,variation,runs,toTest):
    #takes as input minimum and maximum values to choose an integer from
    # runs is the number of runs of dieCalc to perform
    # variation is the acceptable variation from 2.5
    # toTest is the number of dice to test
    # function runs dieCalc (runs) number of times to find how often (dice) die has an average value inside the accepted variation
    #outputs the percent of times that the average value falls inside the accepted variation
    i=0
    minCount= 0
    maxCount= 0
    cur=0
    minVal = 2.5 - variation
    maxVal = 2.5 + variation
    while i < runs:
        cur = dieCalc(min,max,toTest)
        if cur > maxVal:
            maxCount += 1
        elif cur <minVal:
            minCount += 1
        i+=1
#    print(str(minCount/runs))
#    print(str(maxCount/runs))
#    print(str((minCount/runs + maxCount/runs)*100))

#    print(minCount)
#    print(maxCount)
    return 1 - (minCount/runs + maxCount/runs)

def testDies(min,max,runs,accuracy,toTest):
    # takes as input minimum and maximum values to choose an integer from
    # runs is the number of runs of dieCalc to perform, passed to runDies
    # accuracy is the desired % confidence desired for the outputted variance
    # toTest is the number of dice to test
    # function calls and runs runDies to find the minimum variance that fits the desired accuracy and then returns that variance
    # if the function outputs 0.15, need to fix the initial variance (var)
    # for more accurate variations, decrease the step size
    # for faster calculations, increase the step size (will reduce accuracy)
    var = 0.15
    sufficient = False
    while sufficient == False:
        acc = runDies(min,max,var,runs,toTest)
        if acc >= accuracy:
            sufficient = True
        var +=0.01
    return var


# want: some function that: func(acceptable range of accuracy, score to add) = number of rolls to do
    # want: this function to be relatively fast

def  dieCalc2(min,max,dice):
    #takes as input minimum and maximum values to choose an integer from
    # also takes a number of dice to roll
    # runs the specified number of times and outputs the average value outputted by the randint function
    # specific version for findRolls that sums the rolls
    import random
    total=0
    i=0
    while i < dice:
        total += random.randint(min,max)
        i+=1
    return total

def runDies2(min,max,variation,runs,toTest):
    #takes as input minimum and maximum values to choose an integer from
    # runs is the number of runs of dieCalc to perform
    # variation is the acceptable variation from 2.5
    # toTest is the number of dice to test
    # function runs dieCalc (runs) number of times to find how often (dice) die has an average value inside the accepted variation
    #outputs the percent of times that the average value falls inside the accepted variation
        #special version of runDies for findRolls that only finds the percent of times it's over the variation
    i=0
    minCount= 0
    maxCount= 0
    cur=0
    maxVal = 2.5 + variation
    while i < runs:
        cur = dieCalc(min,max,toTest)
        if cur > maxVal:
            maxCount += 1
        i+=1
    return 1 - (maxCount/runs)

def findRolls(accuracy, myscore):
    # takes as input minimum and maximum values to choose an integer from
    # accuracy is the minimum required accuracy (needs to hit final score or less accuracy % of the time)
    # myscore is the player's current score
    # will output the number of rolls so that accuracy % of the time the player's score plus the sum of the die rolled will be at max 100
    return None
