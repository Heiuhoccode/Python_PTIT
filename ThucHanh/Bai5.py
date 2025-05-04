def process(n, p):
    x = 0
    temp = p
    while temp <= n:
        x += n // temp
        temp *= p
    return x

for t in range(int(input())):
    n,p = map(int,input().split())
    print(process(n, p))
