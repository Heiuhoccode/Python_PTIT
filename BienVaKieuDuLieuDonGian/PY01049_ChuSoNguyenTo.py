import math


def snt(u):
    if u < 2: return False
    for i in range(2,int(math.sqrt(u))+1):
        if u%i==0: return False
    return True
def check(u):
    if snt(len(u)) == False:
        return False
    count = 0
    for i in u:
        if(snt(int(i))):
            count += 1
    if count <= len(u)/2:
        return False
    return True

for t in range(int(input())):
    if(check(input())): print("YES")
    else: print("NO")
