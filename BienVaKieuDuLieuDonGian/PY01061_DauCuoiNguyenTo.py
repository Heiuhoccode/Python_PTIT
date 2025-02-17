import math


def isPrime(u):
    if u < 2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u % i ==0: return False
    return True

for t in range(int(input())):
    number = input()
    newNumber1 = number[0:3]
    newNumber2 = number[len(number)-3:]
    print("YES") if isPrime(int(newNumber1)) and isPrime(int(newNumber2)) else print("NO")
# 3
# 12743
# 7337
# 12345678901234