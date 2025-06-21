import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n%i==0: return False
    return True
snt = []
for i in range(2, 100000):
    if isPrime(i):
        dao_i = int(str(i)[::-1])
        if isPrime(dao_i) and i != dao_i:
            snt.append(i)
for i in range(int(input())):
    n = int(input())
    chuaxet = {}
    for a in snt:
        dao_a = int(str(a)[::-1])
        if a not in chuaxet and dao_a not in chuaxet and dao_a<n and a<n:
            print(a, dao_a, end=' ')
            chuaxet[a]=1
            chuaxet[dao_a]=1
    print()

