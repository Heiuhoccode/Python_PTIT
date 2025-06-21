import math


def isPrime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0: return False
    return True
n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in a:
    if isPrime(i): dic[i] = dic.get(i,0) + 1
for i in dic.keys():
    print(f'{i} {dic[i]}')
# 10
# 2 4 7 5 7 8 9 3 7 2