import math
from itertools import combinations

def check(a,b,c):
    if(math.gcd(a,b)!=1 or math.gcd(b,c)!=1 or math.gcd(a,c)!=1):
        return False
    return True

l, r = map(int,input().split())
for i1 in range(l,r-1):
    for i2 in range(i1+1, r):
        for i3 in range(i2+1, r+1):
            if(check(i1,i2,i3)):
                print("({}, {}, {})".format(i1,i2,i3))