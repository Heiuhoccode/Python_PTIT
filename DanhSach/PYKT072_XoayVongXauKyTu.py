def change(s):
    snew = s[1:] + s[0]
    return snew
def process(a,i,n):
    samp = a[i]
    sum = 0
    for j in a:
        cnt = 0
        while samp != j:
            if cnt >= len(j): return -1
            j = change(j)
            cnt += 1
        sum += cnt
    return sum

n = int(input())
a = []
for _ in range(n):
    a.append(input())
minn = 10**6
cnt = 0
for i in range(n):
    cnt = process(a,i,n)
    if cnt == -1:
        break
    else:
        if minn > cnt: minn = cnt

if cnt == -1:
    print(cnt)
else: print(minn)

# 4
# xzzwo
# zwoxz
# zzwox
# xzzwo