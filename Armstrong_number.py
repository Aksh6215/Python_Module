'''
Check whether the given number is armstrong number or not. A number that is equal to the sum of its own digits each raised to the power of the number of digits.
e.g. 
num = 153
explanation:
1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153. Hence, this is an armstrong number.

num = 9474
explanation:
9**4 + 4**4 + 7**4 + 4**4 = 9474. Hence, this is an armstrong number.

num = 1234
explanation:
It is not an armstrong number because the sum of its raised power is 354 which is not equal to 1234.
'''

n = int(input())
# temp = n

def armstrong_number(num):
    power = len(str(num))
    sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + rem ** power
        num = num // 10
    return sum

if armstrong_number(n) == n:
    print("It is an Armstrong number.")
else:
    print("Not an Armstrong number.")