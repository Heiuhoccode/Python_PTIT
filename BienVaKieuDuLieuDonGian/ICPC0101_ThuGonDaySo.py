n = input()
arr = list(map(int,input().split()))
res = []
for i in arr:
    if len(res) == 0 or (res[-1]+i)&1:
        res.append(i)
    else:
        res.pop(-1)
print(len(res))