
'''An ordered collection of items where the addition of new items and the removal of
exsisting items always takes place at the same end, (i.e. last in first out).The output
should be True, 3, 2'''

class Stack:
    def __init__(self): #Assigns values to the object properties of the class
        self.items = [] #Empty array

    def push(self, item): #Adds an item to the top of the stack
        self.items.append(item)

    def pop(self): #Removes item from the top of the stack
        return self.items.pop()

    def empty(self): #Returns a boolean value
        return self.items == []

    def count(self): #Returns number of items in the stack
        return len(self.items)

s = Stack() #Accsesses class
print(s.empty()) #Calls empty method
s.push(1) #Calls push method
s.push('string')
s.push(3)
print(s.pop()) #Displays last item removed
print(s.count()) #Calls count method