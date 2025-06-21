def tohop2 (n):
    if n<2: return 0
    return (n*(n-1)) // 2
n = int(input())
a = []
for i in range(n):
    a.append(input())
sum = 0
for i in a:
    cnt = i.count('C')
    sum += tohop2(cnt)
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j][i] == 'C': cnt+=1
    sum += tohop2(cnt)
print(sum)
# 4
# CC..
# C..C
# .CC.
# .CC.