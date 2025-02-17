from itertools import combinations

n, k = map(int,input().strip().split())
arr = sorted(list({int(i) for i in (input().strip().split())}))
for i in combinations(arr,k):
    print(f"{i[0]} {i[1]} {i[2]}")
# 8 3
# 2 4 4 3 5 1 3 4