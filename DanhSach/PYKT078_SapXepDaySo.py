for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    maxx = max(a)
    b = a[:a.index(maxx)]
    b.append(m)
    for i in a[a.index(maxx):]:
        b.append(i)
    soam,soduong = [],[]
    for i in b:
        if i < 0:
            soam.append(i)
        else: soduong.append(i)
    res = soam + soduong
    for i in res:
        print(i,end=' ')
    print()
