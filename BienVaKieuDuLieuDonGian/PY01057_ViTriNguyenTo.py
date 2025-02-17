import math

def check(s):
    for i in range(len(s)):
        if( (isPrime(i) and not isPrime(int(s[i]))) or (( not isPrime(i) and isPrime(int(s[i])))) ):
            return False
    return True
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
for t in range(int(input())):
    print("YES") if check(input()) else print("NO")