import math


def check(u):
    if u % 3 == 0: return True
    return False
for t in range(int(input())):
    sum = 0
    for i in input():
        sum += ord(i)-48
    if check(sum):
        print("YES")
    else:
        print("NO")
