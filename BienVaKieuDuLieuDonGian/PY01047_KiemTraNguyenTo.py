import math


def snt(u):
    if u < 2:
        return False
    for i in range(2,int(math.sqrt(u))+1):
        if u%i == 0:
            return False
    return True
for t in range(int(input())):
    number = input()
    if(snt(int(number[(len(number)-4)::]))):
        print("YES")
    else:
        print("NO")