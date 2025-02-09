for i in range(int(input())):
    n,x,m=map(float,input().strip().split())
    count = 0
    while(n<m):
        n += float(n*x/100)
        count += 1
    print(count)
