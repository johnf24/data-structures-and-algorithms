
'''A collection of items (nodes) where each item holds a relative position with respect to the others.
The complexity is linear or O(n) in the worst case. The output should be 1, True, False, 3'''

class Node: # Node class
    def __init__(self, initdata): # Assigns values to the properties of the class
        self.data = initdata # List item
        self.next = None # Node reference

# Methods to access and modify the data and the next reference
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

n = Node(1) # Creates node
print(n.getData())


class UnorderedList: # Creates a new empty list
    def __init__(self):
        self.head = None

    def empty(self): # Tests whether the list is empty
        return self.head == None

    def add(self, item): # Adds a new item to the list
        n = Node(item)
        n.setNext(self.head)
        self.head = n

    def size(self): # Returns the number of items in the list
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item): # Searches for the item in the list
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item): # Removes the item from the list
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(3)
mylist.add(1)
mylist.add(2)

mylist.search(2)

mylist.add(4)
print(mylist.search(4))

mylist.remove(4)
print(mylist.search(4))

print(mylist.size())