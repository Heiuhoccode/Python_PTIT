import math
def tong(n):
    return (1+n-1)*(n-1)/2
for _ in range(int(input())):
    n = int(input())
    cnt=0
    for i in range(2,n//2 + 1):
        if (n-tong(i))%i==0 and n-tong(i) > 0:
            cnt+=1
            # print(i)
    print(cnt)