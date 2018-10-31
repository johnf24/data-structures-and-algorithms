
'''An ordered collection of items where the addition of new items happens at the rear and the removal of
exsisting items happens at the front, (i.e. first in first out).The output
should be True, 1, 2'''

class Queue:
    def __init__(self): #Assigns values to the object properties of the class
        self.items = []

    def enqueue(self, item): #Adds a new item to the rear of the queue
        self.items.insert(0, item)

    def dequeue(self): #Removes item from the front of the queue
        return self.items.pop()

    def empty(self): #Returns a boolean value
        return self.items == []

    def count(self): #Returns number of items in the stack
        return len(self.items)

q = Queue() #Accsesses class
print(q.empty()) #Calls empty method
q.enqueue(1) #Calls enqueue method
q.enqueue('string')
q.enqueue(3)
print(q.dequeue()) #Calls dequeue method
print(q.count()) #Calls count method