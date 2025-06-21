def tongcs(a):
    sum = 0
    for i in a:
        sum+=int(i)
    return sum
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a, key=lambda x: (tongcs(str(x)), x))
    for i in b:
        print(i,end=' ')
    print()
# 1
# 8
# 143 43 22 99 7 9 1111 10000000