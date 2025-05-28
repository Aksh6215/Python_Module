# Classes in Python
'''
class Arithmetic:
    a = 10
    b = 11

obj = Arithmetic()
print(obj.a)
print(obj.b)
'''

# Storing Student data
'''
class Student:
    def __init__(self, n, r, m):   # Constructor
        print("__init__", id(self))
        self.name = n   # self is a current object
        self.roll_no = r
        self.marks = m

s1 = Student("John", 11, 90)
s2 = Student("Anoop", 12, 56)
# s1 = Student("Raghav", 43, 57)

print("s1", id(s1))
print("s2", id(s2))

# print(s1.name)
'''

# Another Example of class
'''
class Employee:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age
    def myfunc(myobject):
        print("Hello!,", myobject.name)
    def __str__(myobject):  # It should return the result
        return f"{myobject.name} age is {myobject.age}"

s1 = Employee("Akash", 56)
print(s1)   # using __str__() get string directly
# s1.myfunc()
'''

# Encapsulation (Using Private VAriable & getter/setter)
'''
class BankAccount:
    def __init__(self, bal):
        self.balance = bal
    def get_balance(self):
        return self.balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid Balance!")
'''

# Access Specifiers(Getter / Setter methods) -> Age Eligibility for voting
'''
class One:
    def __init__(self, name1, age1):
        self.name = name1
        self.__age = age1

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age >= 18:
            self.__age = age
        else:
            print("You are not eligible to vote!")

    def disp(self):
        print(self.name)
        print(self.__age)

ref1 = One("John", 30)
ref1.disp()

ref1.name = "Jerry"
ref1.set_age(45)
ref1.disp()
'''

# Taking input from the user
'''
class One:
    def __init__(self, name1, age1):
        self.name = name1
        self.__age = age1

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age >= 18:
            self.__age = age
        else:   
            self.__age = None
            print("You are not eligible to vote!")

    def disp(self):
        print(self.name)
        print(self.__age)

ref1 = One("John", 30)
ref1.disp()

ref1.name = "Jerry"
a = int(input("Enter age "))
ref1.set_age(a)
ref1.disp() 
'''

# Abstraction 
'''
class Car:
    wheels = 4
    def __init__(self, Brand):
        self.name = Brand

car1 = Car("Toyota")
car2 = Car("Honda")
# Car.wheels = 6
car1.__class__.wheels = 6
print(car1.wheels)
print(car2.wheels)
'''

# File not found error
'''
try:
    file = open("file2.txt", "r")
except:
    print("Please create one file first!")
'''

# Value Error
'''
try: 
    a, b = int(input("Enter the values a/b : "))
    print(a/b)
except:
    print("It is a value error check your data!")
'''

# ZeroDivisionError
'''
try:
    a = int(input("Enter the number: "))
    print(100/a)
except:
    print("Number not divisible by Zero!")
'''    

# Type Error
'''
try:
    a, b = int(input("Enter the number: ").split(" "))
    print(a/b)
except:
    print("This is a type error check your data!")
'''

# IO Error

# Raising exception error
'''
try:
    roll = int(input("Enter roll no : "))
    if roll < 1:
        raise Exception("Exception Raised")
except Exception as e:
        print(e)        
'''

# Calculator using functions
'''
def add(a,b):
        print(a+b)

def subs(a,b):
        print(a-b)

def multi(a,b):
        print(a*b)

def div(a,b):
        print(a/b)

add(4,5)
'''
'''
class Arithmetic:
    def __init__(self):
        print("This is constructor")
    def add():
        print("This is addition")
    def subs():
        print("This is substraction")
    def multiply():
        print("This is multiply")
    def div():
        print("This is division")

Arithmetic.add()
'''
'''
class Account:
    def __init__(self, a):
        self.accno = a
        self.__balance = 0

    # def get (self):

obj = Account(1001)
# print(obj.accno)
print(obj._Account__balance)    # We can access the private variable of a class by add class name and that private variable  and this is called as "Name Mangling", but not to use this in your code as it is not a good practice.
'''
'''
# print(dir(int))    # this is magic method list

class fraction:
    def __init__ (self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, obj):
        temp = fraction(0,0)
        temp.num = self.num * obj.den + self.den * obj.num
        temp.den = self.den * obj.den
        return temp
    
x = fraction(3,4)
y = fraction(5,6)
print(x+y)
'''
'''
try:
    print("1")
except:
    print("2")
else:
    print("3")
finally:
    print("Hello")
'''

'''
Que. ARS Gems Store sells different varieties of gems to its customers.
'''
'''
gems_names = ["Diamond", "Ruby", "Emerald"]
gems_price = [9000, 8000, 7000]
gems_quantity = [5, 4, 6]
gems_req = {
    "Diamond" : 6,
    "Ruby" : 4,
    "Emerald" : 6
}
BillAmount = 0
def bill():
    i = 0
    idx = "Diamond"
    global BillAmount
    # for idx in gems_req:
    if gems_req[idx] == gems_quantity[i]:
           BillAmount += gems_quantity[i] * gems_price[i]
           return BillAmount
    else:
        BillAmount = -1
        return BillAmount

Amount = int(bill())
if Amount > 30000:
    Amount = Amount - (Amount * (5/100))
    print(Amount)
else:
     print(Amount)
'''