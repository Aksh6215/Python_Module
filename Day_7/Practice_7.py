'''
# __new__() method

class A(object):
    def __new__(cls):
        print("Creating instance")
        return object.__new__(cls)     # By this we are taking control to creation of the object, if this object is not created then __init__ will not execute.
    def __init__(self):
        print("Init is called")

A()
'''


# Inheritance
'''
# When derived class do not have any constructor then only parent's constructor gets inherited or called.
class Student:
    def __init__(self, name, rollno, marks):
        self.__name = name
        self._rollno = rollno
        self.marks = marks

class Btech(Student):   # Inheriting the Student(Parent) class to Btech(Derived) class
    pass
    
obj = Btech("Aksh", 3, 89)
print(obj.marks)
print(obj._rollno)
print(obj.__name)
'''
'''
class Student:
    def __init__(self, name, rollno, marks):
        self.__name = name
        self.rollno = rollno
        self.marks = marks

    def get_name(self):
        return self.__name

class Btech(Student):  
    def __init__(self, name, rollno, marks, marks_12th):
        Student.__init__(self, name, rollno, marks)     # Calling constructor of parent class
        # super().__init__(name, rollno, marks)     # Super() is also used to call the constructor, but self is not required in super().
        self.marks_12th = marks_12th
    
obj1 = Student("Aksh", 3, 89)
obj2 = Btech("Aman", 1, 78, 89)

print(obj1.get_name(), obj1.marks, obj1.rollno)
print(obj2.get_name(), obj2.marks, obj2.rollno)
'''

# Multiple Inheritance
'''
class Base1():
    def __init__(self):
        print("Base1 init")

class Base2():
    def __init__(self):
        print("Base2 init")
# Sequence of inheritance decides which constructor gets called
# This is called as MRO (Method Resolution Order)
class Derived(Base2, Base1):
    def __init__(self):
        pass

obj = Derived()
print(obj)
'''

'''
class Base1():
    def __init__(self):
        self._str1 = "Base1"
        print("Base1 init")

class Base2():
    def __init__(self):
        self._str2 = "Base2"
        print("Base2 init")

class Derived(Base2, Base1):
    def __init__(self):
        # You can call constructor in manner which you want to get first
        Base2.__init__(self)
        Base1.__init__(self)
        print("Derived")

    def printStr(self):
        print(self._str1, self._str2)

obj = Derived()
obj.printStr()
'''

# Multilevel Inheritance
'''
class Car():
    def __init__(self):
        print("This is the base class.")

class tesla(Car):
    def __init__(self):
        Car.__init__(self)
        print("this ia a tesla.")

class honda(tesla):
    def __init__(self):
        tesla.__init__(self)
        print("this is a honda.")

obj = honda()
print(obj)
'''

# Hybrid Inheritance
'''
class Car():
    def __init__(self):
        print("This is the base class.")

class tesla(Car):
    def __init__(self):
        # Car.__init__(self)
        print("this ia a tesla.")

class honda(tesla):
    def __init__(self):
        Car.__init__(self)
        tesla.__init__(self)
        print("this is a honda.")

obj = honda()
print(obj)
'''
# Abstract Class
'''
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod     # Decorator
    def speak(self):    # Abstract method(must be implemented in subclasses)
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

obj = Cat().speak()
print(obj)
# obj1 = Animal()
obj2 = Dog().speak()
print(obj2)
'''
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def brand(self):
        pass

    def type(self):
        print("Car or Bike")

class Car(Vehicle):
    def brand(self):
        print("Tesla")

obj = Car()'''


# Polymorphism 
# Method Overriding



# Operator Overloading -> it provides built-in support
# User defined : using magic method

# User defined Decorator
'''
def my_decorator(func):     # Decorator must contain wrapper method
    def wrapper():
        print("*****************")
        func()
        print("*****************")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
'''
'''
def my_decorator(func):  
    # to get the arguments by the function in variable length as it can be of any length   
    def wrapper(*args):     
        print("*****************")
        print(args)
        print("*****************")
        return func(*args)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(2, 6))
'''
# Application of the decorator
# Find the time taken by any function for execution
'''
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def add():
    a = 8
    b = 1
    return a+b

ser = add()
print(add())
'''