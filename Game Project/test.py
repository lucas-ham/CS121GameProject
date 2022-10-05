import time
def test():
    if input('String choice') or time.sleep(5):
        return True
    else:
        return False


def test2():
    end = True
    startTime = time.time()
    while end:
        checkTime = time.time()
        if checkTime - startTime < 5:

            
