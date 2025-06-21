def check(n,cnt):
    if n == 1: return cnt
    elif n%2==0: check(n//2,cnt+1)
    elif n%2!=0: check(n*3+1, cnt+1)
while True:
    n = int(input())
    if n == 0: break
    cnt=1
    while n!=1:
        if n%2==0:
            n = n//2
            cnt += 1
        else:
            n=n*3+1
            cnt+=1
    print(cnt)