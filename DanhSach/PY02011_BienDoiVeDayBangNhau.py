n = int(input())
a = list(map(int,input().split()))
minn = 100000
res = {}
for i in a:
    cnt=0
    for j in a:
        cnt+=abs(i-j)
    if minn > cnt:
        minn = cnt
        res[i]=minn
print(minn, end=' ')
for i in res.keys():
    if res[i]==minn:
        print(i)
        break
# 8
# 1 2 2 2 2 2 2 3