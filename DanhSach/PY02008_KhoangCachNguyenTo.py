import math


def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True
snt = []
n,x = map(int,input().split())
for i in range(2,100000):
    if isPrime(i): snt.append(i)
print(x,end=' ')
for i in range(n):
    x = x + snt[i]
    print(x, end=' ')