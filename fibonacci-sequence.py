'''A program that displays the Fibonacci sequence up to nth term. A Fibonacci sequence is the sum of the
two preceding numbers. The output should be 0, 1, 1, 2, 3.'''

n1 = 0
n2 = 1
count = 0
terms = 5

if terms >= 0:
   while count < terms:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1