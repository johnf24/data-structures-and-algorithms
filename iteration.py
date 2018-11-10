
'''A process of repition yields results successively closer to a desired result. The output should be 9'''

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5]))