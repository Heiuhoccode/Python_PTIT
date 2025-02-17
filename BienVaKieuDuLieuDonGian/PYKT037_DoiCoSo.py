def doicoso(n,k):
    origin = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n>0:
        result = origin[n%k] + result
        n //= k
    return result
for t in range(int(input())):
    n, k = map(int,input().strip().split())
    print(doicoso(n,k))
# 3
# 10 2
# 2021 2
# 31 16