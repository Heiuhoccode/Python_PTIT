for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    d = {}
    for i in arr:
        d[i] = d.get(i,0) + 1
    so = sorted(d.keys(), key=lambda x: (-d[x], x))
    temp=1
    for i in so:
        if d[i] > n/2:
            print(f'{i}')
            temp=0
            break
    if temp==1:
        print("NO")
# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4