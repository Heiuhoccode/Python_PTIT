import math

def songuyento(n):
    if (n<2):
        return False
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True

test = int(input())
for i in  range(test):
    n = int(input())
    count = 0
    for i1 in range(n):
        if(math.gcd(i1,n) == 1):
            count += 1
    if(songuyento(count)):
        print("YES")
    else:
        print("NO")
