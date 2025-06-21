def check(a,b,n):
    for i in range(n):
        if a[i] > b[i]: return "NO"
    return "YES"
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    print(check(a,b,n))

# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84