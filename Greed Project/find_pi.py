import random
def throw_pie():
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2+y**2<1:
        return True # Hit
    else:
        return False # Miss

def for_pi(numThrows):
    made = 0
    L = [None]*numThrows
    for index in L:
        if throw_pie():
            made +=1
    return [made, numThrows, 4*(made/numThrows)]

def while_pi(tolError):
    import math
    made = 0
    throws = 0
    estimate = 0
    while abs(math.pi - estimate)>=tolError:
        if throw_pie():
            made +=1
        throws += 1
        estimate = 4*(made/throws)
    return [made, throws, estimate]
