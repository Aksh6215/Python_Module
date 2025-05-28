# Even number Using Function
'''
def find_even(n):
    return n % 2 == 0

l1 = [1,2,3,45,68,88,9]
l2 = list(filter(find_even, l1))
print("Filtered list : ", l2)
'''

# Even number Using Lambda
'''
l1 = [1,2,3,45,68,88,9]
l2 = list(filter(lambda n: n%2 == 0, l1))
print("Filtered list : ", l2)
'''

# Finding all non-zero elements using lambda function
'''
l1 = [1,2,3,44,0,5,60,0]
l2 = list(filter(lambda n:n != 0, l1))
print(l2)
'''

# Finding all non-zero elements using function
'''
def non_zero(n):
    return n != 0
l1 = [1,2,3,44,0,5,60,0]
l2 = list(filter(non_zero, l1))
print("Non-zero elements are :", l2)
'''

# Separating postiive and negative numbers
'''
l1 = [1,-3,4,6,-5,-7]
l2 = (list(filter(lambda n: n >= 0, l1)))
l3 = (list(filter(lambda n: n < 0, l1)))
print("Positive numbers :", l2, "\nNegative numbers :", l3)
'''

# Find Palindrome strings using function and filter
'''
def palindrome(n):
    return n == n[::-1]

l1 = ['aba', 'aaa', 'asd', 'hah', 'wer']
l2 = list(filter(palindrome, l1))
print(l2)
'''

# find Palindrome strings without filter
'''
def palindrome(n):
    return n == n[::-1]
l1 = ['aba', 'aaa', 'asd', 'hah', 'wer']
l2 = []
for i in l1:
    if palindrome(i):
        l2.append(i)

print(l2)
'''

# Map() using function for squaring elements of list
'''
def f1(n):
    return n*2

l1 = [1,2,3,4,5,6]
l2 = list(map(f1, l1))
print("Squared list : ",l2)
'''

# Calculate percentage of marks of 5 students out of 1000

# l1 = [800, 900, 700, 999, 898]
# l2 = list(filter(lambda n, l1))
# print("Percentage : ", l2)

# Reduce()
'''
import functools
l1 = [1,2,3,4,5,6,10]
sum = functools.reduce(lambda a,b:a+b, l1)
print(sum)

import functools
l1 = ['a','b','cde']
sum = functools.reduce(lambda a,b:a+b, l1)
print(sum)
'''
# Using user defined module to get the result
'''
import Module_1
i = int(input("Enter first number : "))
j = int(input("ENter second number : "))
res = Module_1.add(i,j)
print("Addition is :", res)
'''

# Built-in Module -> datetime

import datetime
'''
a = datetime.datetime.now()
print(a)
print(a.year)
'''
'''
import datetime
x = datetime.datetime(2019,2,19)
y = datetime.time(12,45,34,23)
print(x,y)
'''
'''
from datetime import datetime
print(datetime.strptime('5/5/2019', '%d/%m/%Y'))
'''
'''
def add(a,b):
    return a+b
def sub(c,d):
    return c-d
print(add(3,4,5))'''
