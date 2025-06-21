def process(n,cnt):
    while True:
        if n==1: break
        if n%2==0:
            n = n//2
            cnt+=1
        else:
            n = n*3+1
            cnt+=1
    return cnt
while True:
    n = int(input())
    if n==0: break
    if n==1: print(1)
    else:
        print(process(n,1))

