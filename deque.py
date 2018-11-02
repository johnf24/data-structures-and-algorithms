
'''A double-ended queue where the addition or removal of items happens at the front or the rear.
The output should be True, string, 4, 2'''

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

d = Deque() #Accsesses class
print(d.empty()) #Calls empty method
d.addRear(1) #Calls addRear method
d.addRear('string')
d.addFront(3) #Calls addFront method
d.addFront(4)
print(d.removeRear())
print(d.removeFront())
print(d.count()) #Calls count method