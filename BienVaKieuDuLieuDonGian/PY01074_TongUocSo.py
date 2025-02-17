import math


def process(u):
    sum = 0
    for i in range(2, int(math.sqrt(u))+1):
        while(u%i == 0):
            sum+=i
            u/=i
    if u > 1: sum+=u
    return sum
sum = 0
for t in range(int(input())):
    number = int(input())
    sum += process(number)
print(int(sum))
# 5
# 7
# 9
# 10
# 13
# 100