def process(s,n,a,b,c):
    if len(s) == n and a <=b and b<=c and a>0:
        print(s)
    if len(s) < n:
        process(s + 'A',n,a+1,b,c)
        process(s + 'B',n, a, b + 1, c)
        process(s + 'C',n, a, b, c + 1)
n = int(input())
for i in range(3,n+1):
    process('',n,0,0,0)