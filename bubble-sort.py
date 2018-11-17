
'''The bubble sort makes multiple passes through a list and compares adjacent items
and exchanges those that are out of order. The complexity is Quadratic or O(n2).
The output should be 4, 8, 12, 16, 20.'''

def bubbleSort(alist):
    for x in range(len(alist)-1,0,-1):
        for i in range(x):
            if alist[i]>alist[i+1]:
                temp = alist[i] # Exchange
                alist[i] = alist[i+1] # Temporary storage location
                alist[i+1] = temp
                '''alist1[i], alist1[i+1] = alist1[i+1], alist[i] Optional exchange assignment'''

testlist = [12, 20, 8, 16, 4]
bubbleSort(testlist)
print(testlist)