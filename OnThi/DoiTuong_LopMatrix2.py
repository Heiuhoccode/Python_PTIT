def chuyenvi(a,n,m):
    b = []
    for i in range(m):
        b1 = []
        for j in range(n):
            b1.append(a[j][i])
        b.append(b1)
    return b
def nhan(a,b,n,m):
    c = []
    for i in range(n):
        c1 = []
        for j in range(n):
            temp = 0
            for k in range(m):
                temp += a[i][k]*b[k][j]
            c1.append(str(temp))
        c.append(c1)
    return c
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int,input().split())))
    b = chuyenvi(a,n,m)
    c = nhan(a,b,n,m)
    for i in c:
        print(' '.join(i))