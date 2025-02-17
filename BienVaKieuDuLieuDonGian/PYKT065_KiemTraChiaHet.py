import math


def isPrime(u):
    if u<2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u%i==0: return False
    return True

while(True):
    s = input()
    if(s == '-1'):
        break
    l,r = map(int,s.split())
    n = int(input())
    count = 0
    if l==1: count += 1
    if l<n:
        for i in range(n+1,r+1):
            if isPrime(i): count+=1
    else:
        for i in range(l,r+1):
            if isPrime(i): count+=1
    print(count)