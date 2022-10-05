def myStrategy(myscore, theirscore, last):
    # net best so far
    # might lose to myStrategy4 more often than not
    import random
    def  dieCalc(dice):
        # also takes a number of dice to roll
        # runs the specified number of times and outputs the average value outputted by the randint function
        # function will be called later and used
        total=0
        i=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    def rolls(myscore,rolls):
        i = 0
        add = 0
        while i <rolls:
            add += random.randint(0,5)
            i+=1
        return myscore + add

    myMissing = 100-myscore
    theirMissing = 100-theirscore
    delta = theirscore - myscore

    # some basic cases where the desired result is known/trivial
    if 96 <= myscore:
        # if i'm close to winning i don't want to roll and lose
        if delta < 0:
            return 0
        else:
            return 1
    elif 93 <=myscore:
        if delta > 5:
            return 2
        else:
            return 1
    elif delta < 0 and last == 1:
        return 0

    numDice = int(myMissing/2)
    stop = False
    while stop == False:
        i = 0
        counter = 0
        runs = 500
        while i < runs:
            total=myscore
            total += dieCalc(numDice)
            if total > 100:
                counter = 1
                i=500
            i+=1
        if counter > 0:
            numDice += -1
        else:
            stop = True
    return numDice

def manyTests(strat,runs):
    less97 = 0
    less98 = 0
    less100 = 0
    less101 = 0
    less102  = 0
    over105 = 0
    i = 0
    while i < runs:
        flag = True
        score = 0
        while flag==True:
            rolls = strat(score,0,0)
            j = 0
            if rolls == 0:
                flag = False
            else:
                while j<rolls:
                    diceTotal = roll()
                    j += 1
                score += diceTotal
        if score <= 97:
            less97 +=1
        elif score <=98:
            less98 +=1
        elif score <=100:
            less100 +=1
        elif score <= 101:
            less101 +=1
        elif score <=102:
            less102 +=1
        else:
            over105 +=1
        i+=1
    print("less than 97: "+str(less97))
    print("between 97-98: "+str(less98))
    print("between 98-100: "+str(less100))
    print("between 100-101: "+str(less101))
    print("between 101-102: "+str(less102))
    print("over 105: " +str(over105))



def myStrategy2(myscore, theirscore, last):
    numReturn = 0
    if myscore <= theirscore:
        if myscore < theirscore and last:
            numReturn = int((100-myscore)/4)
        elif myscore == theirscore and last:
            numReturn = 0
        elif myscore == theirscore:
            numReturn = int((100-myscore)/3)
    else:
        numReturn = int((100-myscore)/3)
    return numReturn

def myStrategy3(myscore,theirscore,last):
    if myscore >= 95:
        if myscore < theirscore and last:
            return 1
        else:
            return 0
    else:
        import random
        i = 0
        totalCounted = 0
        counted = 0
        while i < 100:
            numDice=0
            total = myscore
            while total < 98:
                die = random.randint(0,5)
                total += die
                numDice += 1
            i+=1
            if total < 100:
                counted += 1
                totalCounted += numDice
                #qprint(totalCounted,numDice)
        return int(totalCounted/counted)

def myStrategy4(myscore,theirscore,last):
    #how is this my T1st strategy?
    #might even be a little better than myStrategy, close
    delta = 100-myscore
    if delta <= 5:
        return int(delta/4)
    elif delta <=15:
        return int(delta/3.85)
    elif delta <=25:
        return int(delta/3.75)
    elif delta > 25:
        return int((100-myscore)/3.5)

def myStrategy5(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    options[0] = int(delta/3)
    options[1] = int(delta/3.25)
    options[2] = int(delta/3.5)
    options[3] = int(delta/3.75)
    options[4] = int(delta/4)
    while i < 3:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/3)
    dice = int(sum(D)/3)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(itn(delta/3),1)
        else:
            dice =0
    return dice


def myStrategy6(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore and last:
        options[0] = int(delta/2.5)
        options[1] = int(delta/3)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 3:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/3)
    dice = int(sum(D)/3)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(itn(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy7(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore:
        if last:
            options[0] = int(delta/2.5)
            options[1] = int(delta/3)
            options[2] = int(delta/3.5)
            options[3] = int(delta/3.75)
            options[4] = int(delta/4)
        else:
            options[0] = int(delta/2.5)
            options[1] = int(delta/3)
            options[2] = int(delta/3.5)
            options[3] = int(delta/3.75)
            options[4] = int(delta/4)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 3:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/3)
    dice = int(sum(D)/3)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(itn(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy8(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    options[0] = int(delta/3)
    options[1] = int(delta/3.25)
    options[2] = int(delta/3.5)
    options[3] = int(delta/3.75)
    options[4] = int(delta/4)
    while i < 3:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/3)
    dice = int(sum(D)/3)
    return dice

def myStrategy9(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore and last:
        options[0] = int(delta/2.5)
        options[1] = int(delta/3)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 2:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/2)
    dice = int(sum(D)/2)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(int(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy10(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    if last and myscore >= theirscore:
        if myscore > theirscore or (myscore >= 98):
            return 0
        if myscore >= 92:
            return 1
        if myscore >= 88:
            return 2
        if myscore >= 81:
            return 3
        return 4
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore and last:
        options[0] = int(delta/2.5)
        options[1] = int(delta/3)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 3:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/3)
    dice = int(sum(D)/3)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(itn(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy11(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore and last:
        options[0] = int(delta/2.5)
        options[1] = int(delta/3)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    elif myscore > theirscore:
        options[0] = int(delta/3.15)
        options[1] = int(delta/3.3)
        options[2] = int(delta/3.45)
        options[3] = int(delta/3.6)
        options[4] = int(delta/3.75)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 2:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/2)
    dice = int(sum(D)/2)
    if  val == myscore and last:
        if myscore < theirscore:
            dice = max(int(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy12(myscore, theirscore, last):
    import random
    def rolls(myscore,rolls):
        i = 0
        add = 0
        while i <rolls:
            add += random.randint(0,5)
            i+=1
        return myscore + add
    dice6 = myStrategy6(myscore,theirscore,last)
    dice10 = myStrategy10(myscore,theirscore,last)
    dice11 = myStrategy11(myscore,theirscore,last)
    from6 = rolls(myscore,dice6)
    from10 = rolls(myscore,dice10)
    from11 = rolls(myscore,dice11)
    if from6 >100:
        from6 = 0
    elif from10 >100:
        from10 = 0
    elif from11 >100:
        from11= 0

    if from6>from10:
        if from6>from11:
            return dice6
        elif from11 >from10:
            return dice10
    elif from10>from11:
        return dice10
    else:
        return dice11

def myStrategy13(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    import random
    if last and myscore >= theirscore:
        if myscore > theirscore or (myscore >= 98):
            return 0
        if myscore >= 92:
            return 1
        if myscore >= 88:
            return 2
        if myscore >= 81:
            return 3
        return 4
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total
    D =[]
    V =[]
    delta = 100-myscore
    options=[0,0,0,0,0]
    i = 0
    if myscore<theirscore and last:
        options[0] = int(delta/2.5)
        options[1] = int(delta/3)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    elif myscore > theirscore:
        options[0] = int(delta/3.15)
        options[1] = int(delta/3.3)
        options[2] = int(delta/3.45)
        options[3] = int(delta/3.6)
        options[4] = int(delta/3.75)
    else:
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
    while i < 2:
        values = [roll(x) + myscore for x in options]
        saveVals = values
        #print(options)
        #print(values)
        end = True
        if min(options) == max(options):
            #return options[0]
            D.append(options[0])
            V.append(values[0])
        elif min(values) > 100:
            #return 0
            D.append(0)
            V.append(0)
        else:
            while end:
                if max(values) >100:
                    values.remove(max(values))
                else:
                    index=values.index(max(values))
                    #return options[index]
                    D.append(options[index])
                    V.append(max(values))
                    end = False
        i+=1
    val = int(sum(V)/2)
    dice = int(sum(D)/2)
    if  val < myscore and last:
        if myscore < theirscore:
            dice = max(int(delta/3),1)
        else:
            dice =0
    return dice

def myStrategy16(myscore,theirscore,last):
    # just gonna manually add more tests to myStrategy5
    # will (hopefully) give it better results and closer to desired
    # weird that this one doesn't beat myStrategy5, same algorithm just has more options
    # maybe will recreate this one but more exact to the code of myStrategy5
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total

    delta = 100-myscore
    options=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    options[0] = int(delta/2.5)
    options[1] = int(delta/2.65)
    options[2] = int(delta/2.8)
    options[3] = int(delta/2.95)
    options[4] = int(delta/3.1)
    options[5] = int(delta/3.25)
    options[6] = int(delta/3.4)
    options[7] = int(delta/3.55)
    options[8] = int(delta/3.75)
    options[9] = int(delta/4)
    options[10] = int(delta/4.15)
    options[11] = int(delta/4.3)
    options[12] = int(delta/4.45)
    options[13] = int(delta/4.6)
    options[14] = int(delta/4.75)
    rolls = [roll(x) for x in options]
    values = [x + myscore for x in rolls]
    saveVals = values
    #print(options)
    #print(values)
    end = False
    if min(options) == max(options):
        return options[0]
    elif min(values) > 100:
        return 0
    else:
        while end == False:
            if max(values) >=100:
                values.remove(max(values))
            else:
            #    print(max(values))
                index=values.index(max(values))
                returnVal = options[index]
                end = True
    if max(values) >97:
        if myscore <= 90:
            return returnVal - 3

    if last and theirscore > max(values):
        return returnVal + 1
    else:
        return returnVal



def myStrategy17(myscore,theirscore,last):
    def myStrategy5Val(myscore,theirscore,last):
        # interesting working with lists
        # pretty solid strategy
        # can add more to options to make better predictions
        # best Strategy so far, and FAST
        def roll(dice):
            i=0
            total=0
            while i < dice:
                total += random.randint(0,5)
                i+=1
            return total

        delta = 100-myscore
        options=[0,0,0,0,0]
        options[0] = int(delta/3)
        options[1] = int(delta/3.25)
        options[2] = int(delta/3.5)
        options[3] = int(delta/3.75)
        options[4] = int(delta/4)
        rolls = [roll(x) for x in options]
        values = [x + myscore for x in rolls]
        saveVals = values
        #print(options)
        #print(values)
        end = False
        if min(options) == max(options):
            return [options[0],max(values)]
        elif min(values) > 100:
            return [0,myscore]
        else:
            while end == False:
                if max(values) >100:
                    values.remove(max(values))
                else:
                #    print(max(values))
                    index=values.index(max(values))
                #    print(options[index])
                    return [options[index],max(values)]

    def myStrategy6Val(myscore,theirscore,last):
        # just gonna manually add more tests to myStrategy5
        # will (hopefully) give it better results and closer to desired
        def roll(dice):
            i=0
            total=0
            while i < dice:
                total += random.randint(0,5)
                i+=1
            return total

        delta = 100-myscore
        options=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        options[0] = int(delta/2.5)
        options[1] = int(delta/2.65)
        options[2] = int(delta/2.8)
        options[3] = int(delta/2.95)
        options[4] = int(delta/3.1)
        options[5] = int(delta/3.25)
        options[6] = int(delta/3.4)
        options[7] = int(delta/3.55)
        options[8] = int(delta/3.75)
        options[9] = int(delta/4)
        options[10] = int(delta/4.15)
        options[11] = int(delta/4.3)
        options[12] = int(delta/4.45)
        options[13] = int(delta/4.6)
        options[14] = int(delta/4.75)
        rolls = [roll(x) for x in options]
        values = [x + myscore for x in rolls]
        saveVals = values
        #print(options)
        #print(values)
        end = False
        if min(options) == max(options):
            return [options[0],max(values)]
        elif min(values) > 100:
            return [0,myscore]
        else:
            while end == False:
                if max(values) >=100:
                    values.remove(max(values))
                else:
                #    print(max(values))
                    index=values.index(max(values))
                    returnVal = options[index]
                    end = True
        if max(values) >97:
            if myscore <= 90:
                return [returnVal - 3, max(values)]

        if last and theirscore > max(values):
            return [returnVal + 1,max(values)]
        else:
            return [returnVal, max(values)]
    from5 = myStrategy5Val(myscore,theirscore,last)
    from6 = myStrategy6Val(myscore,theirscore,last)
    rolls5 = int(from5[0])
    value5 = int(from5[1])
    rolls6 = int(from6[0])
    value6 = int(from6[1])
    if value5 >=100:
        if value6 >=100:
            return 0
        else:
            return rolls6
    elif value6 >=100:
        return rolls5
    elif value5>=value6:
        return rolls5
    else:
        return rolls6


def myStrategy18(myscore,theirscore,last):
    # interesting working with lists
    # pretty solid strategy
    # can add more to options to make better predictions
    # best Strategy so far, and FAST
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total

    delta = 100-myscore
    options=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    options[0] = int(delta/2.5)
    options[1] = int(delta/2.65)
    options[2] = int(delta/2.8)
    options[3] = int(delta/2.95)
    options[4] = int(delta/3.1)
    options[5] = int(delta/3.25)
    options[6] = int(delta/3.4)
    options[7] = int(delta/3.55)
    options[8] = int(delta/3.75)
    options[9] = int(delta/4)
    options[10] = int(delta/4.15)
    options[11] = int(delta/4.3)
    options[12] = int(delta/4.45)
    options[13] = int(delta/4.6)
    options[14] = int(delta/4.75)
    rolls = [roll(x) for x in options]
    values = [x + myscore for x in rolls]
    saveVals = values
    print(options)
    print(values)
    end = False
    if min(options) == max(options):
        return options[0]
    elif min(values) > 100:
        return 0
    elif max(options) <=3:
        while end == False:
            if max(values) >100:
                values.remove(max(values))
            else:
            #    print(max(values))
                index=values.index(max(values))
            #    print(options[index])
                if len(values)<=8:
                    return options[index]-1
                else:
                    return options[index]

    else:
        while end == False:
            if max(values) >100:
                values.remove(max(values))
            else:
            #    print(max(values))
                index=values.index(max(values))
            #    print(options[index])
                return options[index]

def myStrategy19(myscore,theirscore,last):
    # trying to make strat5 better
    # obscuring number to make it easier to have more options
    # getting a float error despite no floats
    def roll(dice):
        i=0
        total=0
        while i < dice:
            total += random.randint(0,5)
            i+=1
        return total

    delta = 100-myscore
    options=[0,0,0,0,0]
    n = 5
    i = 1
    min = 2.5
    max = 3.5
    step = (max-min)/n
    increase = 0
    while i <= n:
        options[i-1] = int(delta/(2.5 + increase))
        increase += step
        i+=1
    rolls = [roll(x) for x in options]
    values = [x + myscore for x in rolls]
    saveVals = values
    min(float(sub) for sub in values)
    return None





    # average value of random.randint(0,5) = 2.5
    # for 40 dies, less than 0.35 variance 80% of the time
        # aka, 80% of the time when rolling 40 dies the average value falls between 2.15 and 2.85
    # accurate between 1.49 and 3.51 95% of time when rolling 10 die
    # accurate between 1.74 and 3.26 95% of time when rolling 20 die
        # this means that 95% of the time, rolling 20 dies will give a max score of 70.2

# accurate between 1.84 and 3.16 90% of time when rolling 20 die

    #ALL ACCURACY PREDICTIONS MADE WITH FILE (SELF WRITTEN) TITLED dieCalc.py CAN SUBMIT IF NECESSARY
