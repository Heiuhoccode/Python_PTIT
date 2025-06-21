import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n%i==0: return False
    return True

n = int(input())
a = list(map(int,input().split()))
d = {}
for i in a:
    if isPrime(i):
        d[i] = d.get(i,0)+1
for i in d:
    print(f'{i} {d[i]}')

# 10
# 2 4 7 5 7 8 9 3 7 2