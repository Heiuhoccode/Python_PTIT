import math


def ntcn(a,b):
    if math.gcd(a,b) == 1: return True
    return False
n = int(input())
arr = sorted(list(map(int,input().split())))
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if ntcn(arr[i],arr[j]):
            print(f'{arr[i]} {arr[j]}')