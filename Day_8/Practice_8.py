# datetime library

# from datetime import datetime


# calendar library
# import calendar

# calendar.prcal(2002)

# glob library

# import sys
'''import glob

files = glob.glob("*/**.txt")
print(files)'''

# pickle and json library

# iterators
'''
list = [1,2,3,4]

iterator = iter(list)   # Getting an iterator object

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))   # Raises exception StopIteration
'''

'''
list = [x for x in range(1, 10000)]

import sys
print(sys.getsizeof(list))

a = range(1, 10000)
print(sys.getsizeof(a))

# Main use of iterator is to get single element at a time to reduce the memory space in system
'''
'''
# checking that it is iterable or not

a = {}
print(dir(a))
'''

# create own iterators
'''
def func(iterable):
    iterator = iter(iterable)
    while True:
        try: 
            print(next(iterator))
        except StopIteration:
            break

list = [1,2,3]
tuple = (5,6,7)
set = {8,9,0}
dict = {1:1, 2:4, 3:9}

func(list)
'''


# Generator
# creating a generator using function -> first method
'''
def generator_fun():    # multiple values can be returned through generator
    yield "First";
    yield "Second";
    yield "Third"

gen = generator_fun()   # Calling function
print(next(gen))    
print(next(gen))

next(generator_fun())   # new instance get generated if you call the function again
print(next(gen))
'''

# Generate suqares of a series
'''
def squr():
    for i in range(1, 21):
        res = i ** 2
        yield res

gen = squr()
print(gen)      # it will give the generator object
print(next(gen))
'''
# Generator for fibonacci series

# Generating own range function
'''
def range_func(start, end):
    for i in range(start, end):
        yield i

gen = range_func(5, 11)
print(next(gen))
print("Inside for loop.")

for i in gen:
    print(i)
'''

# Creating a generator using expression 
# generator can be generrated by just replacing the square brackets with parenthesis
'''
list = [i ** 2 for i in range(1, 100)]
import sys
print(sys.getsizeof(list))

print(list)
'''
'''
list = (i ** 2 for i in range(1, 100))  # optimize the memory
import sys
print(sys.getsizeof(list))
'''

# Regular Expression
# Searching for a number in a text
'''
import re

text = "Hello my number is 8000621560, with roll no 07 and rtu 21EJCAD007"
pattern = r'\d+'
# Searching for pattern in the text
match = re.search(pattern, text)

print(re.findall(pattern, text), "\n")  # will give complete info about that
print(match.group())    # provide the pattern
'''
'''
import re

text = "Hello my number is 8000621560, with roll no 07 and rtu 21EJCAD007"
pattern = r'\d+'
match = re.match(pattern, text)

print(re.search(pattern, text))
'''
'''
import re
text = "(999)789-543"
pattern = r'\(\d{3}\)\d{3}-\d{3}' # for inserting parenthesis use \(\)

match = re.match(pattern, text)
print(match)
'''