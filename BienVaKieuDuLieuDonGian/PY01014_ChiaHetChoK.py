a,k,n = map(int,input().strip().split())
cnt=0
for i in range(n-a):
    if((a+i)%k==0):
        cnt=1
        print(i,end=' ')
if cnt == 0:
    print(-1)