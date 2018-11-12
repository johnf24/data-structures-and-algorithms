
'''A method of solving problems that involves breaking a problem down into smaller subproblems until it
can be solved trivially. This algorithm calculates the sum of a list of numbers. The output should be 9 '''

def listsum(numList):
   if len(numList) == 1: # Base case
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:]) # Function calls itself recursively

print(listsum([1,3,5]))