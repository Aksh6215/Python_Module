def fun(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b

c = int(input("c: "))
a = int(input("a: "))
b = int(input("b: "))
print(fun(a,b,c))