# 1. Calculate the area of the rectangle
'''
l,b = input("Enter the length and breadth : ").split()
print("Area of rectangle =", int(l)*int(b))
'''

# 2. Calculate the Simple Interest & Compound Interest
'''
PrincipalAmt = int(input("Enter the amount : "))
Rate = int(input("Enter the rate of interest : "))
Time = float(input("Enter the time in years : "))
print("Simple Interest is =", (PrincipalAmt*Rate*Time)/100)
print("Compound Interest is =", PrincipalAmt*(1+Rate)**Time - PrincipalAmt)
'''

# 3. Calculate the BMI Index 
'''
weight = input("Enter weight : ")
height = input("Enter height(in cm) : ")
print("BMI = ", (weight/(height/100)**2))
'''

# 4. Basic Arithmetic operations on 3 numbers
'''
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
print("Addition =", a+b+c,"\nMultiplication =", a*b*c)
'''

# 5. Sum of squares of n natural numbers
'''
n = int(input("Enter the number : "))
sum = 0
temp = n
while temp > 0:
    res = temp * temp
    sum += res
    temp -= 1
print("Sum of squares of first", n, "natural numbers is", sum)
'''

# 6. Factorial of a number
'''
n = int(input("Enter a number for factorial : "))

fact = 1
if n == 0 or n == 1:
    print("Factorial is ", fact)
elif n < 0:
    print("Invalid input")
else:
    while n > 0:
        fact = fact * n 
        n -= 1
print("Factorial is", fact)
'''

# 7. Reverse a String
'''
a = input("Enter a string : ")
i = len(a)
while i > 0:
    print(a[i-1], end="")
    i -= 1
'''

# 8. Capitalize alternate characters of a string
'''
str = input("Enter a string : ")
i = 0
while i < len(str):
    if i % 2 == 0:
        print(str[i].upper(), end="")
    else:
        print(str[i], end="")
    i += 1
'''