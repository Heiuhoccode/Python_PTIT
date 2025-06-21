import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n%i==0: return False
    return True
for _ in range(int(input())):
    cnt=0
    n = int(input())
    for i in range(2,n-6):
        if (isPrime(i) and isPrime(i+2) and isPrime(i+6)) or (isPrime(i) and isPrime(i+4) and isPrime(i+6)):
            cnt+=1
            # print(i, end=' ')
    print(cnt)