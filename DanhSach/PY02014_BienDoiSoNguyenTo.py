import math

def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

snt = []
for i in range(10000):
    if isPrime(i): snt.append(i)
n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    if not isPrime(i):
        b.append(i)
        # a.remove(i)
res = 0
for i in b:
    for j in range(1,len(snt)):
        if snt[j-1] < i < snt[j]:
            res = max(res,min(snt[j]-i, i-snt[j-1]))
            # print(f'{snt[j-1]} - {i} - {snt[j]}')
print(res)

# 8
# 13 5 8 7 9 15 26 34
