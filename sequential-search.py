
'''The sequential search searches a list where the items are in sequntial order. The complexity is liner
or O(n) in the worst case and constant or O(1) in the best case. The output should be False, True.'''

def sequentialSearch(alist, item):
    i = 0
    found = False

    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
        else:
            i = i+1

        return found

testlist = [8, 1, 4, 9, 3]

print(sequentialSearch(testlist, 7))
print(sequentialSearch(testlist, 1))