import math


def isPrime(u):
    if u<2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u%i==0: return False
    return True

for t in range(int(input())):
    number = input()
    count = 0
    for i in number:
        if isPrime(int(i)): count += 1
    print("YES") if isPrime(len(number)) and count > len(number)/2 else print("NO")
# 3
# 1234567
# 22334455667
# 23400300489898989