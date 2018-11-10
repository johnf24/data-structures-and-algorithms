
'''An algorithm where a string of characters is inputed is checked whether it is a palindrome
or a word that reads the same forward or backwards. The output should be False, True'''

class Deque:
    def __init__(self): #Assigns values to the object properties of the class
        self.items = []

    def addFront(self, item): #Adds a new item to the front of the deque
        self.items.append(item)

    def addRear(self, item): #Adds a new item to the rear of the deque
        self.items.insert(0, item)

    def removeFront(self): #Removes the front item from the deque
        return self.items.pop()

    def removeRear(self): #Removes the rear item from the deque
        return self.items.pop(0)

    def empty(self): #Returns a boolean value
        return self.items == []

    def count(self): #Returns number of items in the stack
        return len(self.items)


def palChecker(string): #Checks Palindrome
    check = Deque()

    for i in string: #For loop
        check.addRear(i)

    while check.count() > 1: #While loop
        first = check.removeFront() #Calls removeFront method
        last = check.removeRear() #Calls removeRear method
        if first != last: #Conditional
            equal = False
        else first == last:
            equal = True

    return equal


print(palChecker('fjybsk'))
print(palChecker('radar'))