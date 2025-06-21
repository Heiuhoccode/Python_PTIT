for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in a[k:]:
        b.append(i)
    for i in a[0:k]:
        b.append(i)
    for i in b:
        print(i,end=' ')
# 2
# 5 2
# 1 2 3 4 5
# 10 3
# 2 4 6 8 10 12 14 16 18 20