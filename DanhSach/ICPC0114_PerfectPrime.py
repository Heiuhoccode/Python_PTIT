import math


def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n%i==0: return False
    return True
def check(n):
    if not isPrime(n): return "No"
    if not isPrime(int(str(n)[::-1])): return "No"
    for i in str(n):
        if not isPrime(int(i)): return "No"
    sum = 0
    for i in str(n):
        sum += int(i)
    if not isPrime(sum): return "No"
    return "Yes"
for _ in range(int(input())):
    n = int(input())
    print(check(n))