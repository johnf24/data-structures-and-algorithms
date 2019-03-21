'''A program that displays all the prime numbers within an interval. A prime number is a number greater
than 1 that cannot be formed by multiplying two smaller numbers. The output should be 2, 3, 5'''

lower = 0
upper = 5

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)