F = [0 for _ in range(93)]
F[1]=1
F[2]=1
for i in range(3,93):
    F[i] = F[i-1] + F[i-2]
for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(F[i], end=' ')
    print()