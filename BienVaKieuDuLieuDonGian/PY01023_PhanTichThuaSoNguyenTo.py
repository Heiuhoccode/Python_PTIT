import math

for t in range(int(input())):
    number = int(input())
    res = []
    res1 = []
    temp  = 0
    kq = "1"
    for i in range(2,int(math.sqrt(number))+1):
        while(number%i==0):
            number /= i
            temp=i
            res.append(i)
        if(temp!=0):
            res1.append(temp)
            temp=0
    if(number!=1):
        res.append(int(number))
        res1.append(int(number))
    for i in res1:
        kq = kq + " * " + str(i) + "^" + str(res.count(i))
    print(kq)