# Task 1
size = int(input(""))
numbers = input("").strip().split(" ")
final = []

if len(numbers) == size:
    for i in numbers:
        if int(i)%2 == 0:
            final.append(i)

    for i in numbers:
        if int(i)%2 != 0:
            final.append(i)

for i in final:
    print(i, end=" ")

# Task 2
size = int(input(''))
string = input('')
max_length = 0
if size == len(string):
    m=0
    # Main logic
    for i in range(1,size-1):
        m += 1
        if m > max_length:
            max_length=m
        if string[i]==string[i+1]:
            continue
        else:
            m = 0
print(max_length)

# Task 3
def count_pairs(n,lst):
    l = list(lst)
    colors = set(l)
    sum = 0
    for i in colors:
        sum += (l.count(i)//2)
    return sum
n = 9
l = [10,20,20,10,10,30,50,10,20]
ans = count_pairs(n,l)
print(ans)