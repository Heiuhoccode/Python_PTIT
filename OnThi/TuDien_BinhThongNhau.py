def root(x):
    if binh[x] != x:
        return root(binh[x])
    return x

n = int(input())
binh = list(range(100001))
# print(binh.values())
cnt=1
for _ in range(n):
    x,y,z = map(int,input().split())
    if z == 1:
        goc_x = root(x)
        goc_y = root(y)
        if goc_x != goc_y:
            binh[goc_y] = goc_x
    else:
        if root(x) == root(y):
            print(1)
        else: print(0)
        # print(binh.values())
# 9
# 1 2 2
# 1 2 1
# 3 7 2
# 2 3 1
# 1 3 2
# 2 4 2
# 1 4 1
# 3 4 2
# 1 7 2