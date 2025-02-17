import math

for t in range(int(input())):
    number = input()
    number2 = number[::-1]
    if(math.gcd(int(number),int(number2))==1):
        print("YES")
    else:
        print("NO")