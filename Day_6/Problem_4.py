m = int(input("m = "))
n = int(input("n = "))
# sum = 0

def add():
    if m > 0 and n >= 0:
        for i in range(m, n+1):
            if i%3 == 0 and i%5 == 0:
                global sum
                return sum + i
            else:
                return sum
    
res = int(add())
print(res)
