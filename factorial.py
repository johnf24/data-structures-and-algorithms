'''This is a program to find the factorial of a number. The factorial of a number is the product of all
the integers below it. The output should be 120.'''

num = 5
factorial = 1

if num > 0:
   for i in range(1, num + 1):
       factorial = factorial * i
   print(factorial)