def doChenhLech(a):
    tren,duoi = 0,0
    for i in range(len(a)):
        for j in range(len(a)):
            if j>i: tren += a[i][j]
            elif j<i: duoi += a[i][j]
    return abs(tren-duoi)
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
k = int(input())
DCL = doChenhLech(a)
print("YES" if DCL<=k else "NO")
print(DCL)

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5