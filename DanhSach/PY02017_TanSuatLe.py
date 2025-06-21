for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = {}
    for i in arr:
        a[i] = a.get(i,0) + 1
    for i in a.keys():
        if a[i]%2!=0:
            print(i)
            break
# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2