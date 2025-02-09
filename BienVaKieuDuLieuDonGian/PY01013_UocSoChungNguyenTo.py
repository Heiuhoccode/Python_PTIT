import math


def songuyento(number):
    if(number < 2):
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if(number%i==0):
            return False
    return True

for i in range(int(input())):
    a,b = map(int,input().strip().split())
    ucln = math.gcd(a,b)
    summ = 0
    for u in str(ucln):
        summ += int(u)
    if(songuyento(summ)):
        print("YES")
    else:
        print("NO")