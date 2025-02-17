import math


def check(u):
    if u < 2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u % i == 0: return False
    return True
for t in range(int(input())):
    sum = 0
    for i in input():
        sum += ord(i)-48
    if check(sum):
        print("YES")
    else:
        print("NO")
