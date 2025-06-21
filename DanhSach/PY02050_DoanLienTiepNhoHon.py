for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        cnt = 0
        for j in range(0,i+1):
            if a[j] <= a[i]: cnt += 1
        print(cnt, end=' ')
    print()
# 1
# 7
# 100 80 60 70 60 75 85