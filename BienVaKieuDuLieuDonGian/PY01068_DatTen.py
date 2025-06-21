from itertools import combinations

n,m = map(int, input().split())
a = []
for i in input().split():
    if i not in a:
        a.append(i)
a = sorted(a)
print(a)
tohop = combinations(a, m)
print('\n'.join([' '.join(x) for x in tohop]))
# 6 2
# DONG TAY NAM BAC TAY BAC