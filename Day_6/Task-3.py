
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