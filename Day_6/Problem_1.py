def fun(s,ch1,ch2):
    str = ''
    for i in s:
        if i == ch1:
            str += ch2
        elif i == ch2:
            str += ch1
        else:
            str += i
    return str


s = input('Str: ')
ch1= input('ch1:')
ch2= input('ch2:')
print(fun(s,ch1,ch2))