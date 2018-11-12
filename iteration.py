
'''A process of repition thats yields results successively closer to a desired result. This algorithm
calculates the sum of a list of numbers. The output should be 9'''

def listsum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    return sum

print(listsum([1,3,5]))