
'''The binary search serches a list where the items are in sequntial order but starts at the middle item.
The complexity is Logarithmic or O(log n). The output should be False, True.'''

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

        return found

testlist = [0, 2, 4, 6, 8, 10, 12]

print(binarySearch(testlist, 3))
print(binarySearch(testlist, 6))