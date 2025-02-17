import math


def snt(u):
    if u < 2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u%i==0: return False
    return True
def check(s):
    sum = 0
    for i in range(0, len(s), 2):
        sum += ord(s[i])-48
        if (ord(s[i])-48)%2 != 0: return False
    for i in range(1, len(s), 2):
        sum += ord(s[i]) - 48
        if (ord(s[i])-48)%2 == 0: return False
    if snt(sum) == False: return False
    return True
for t in range(int(input())):
    if check(input()): print("YES")
    else: print("NO")
# 2
# 2345678521
# 1212121212121212121212121