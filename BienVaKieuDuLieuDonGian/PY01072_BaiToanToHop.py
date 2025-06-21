from itertools import combinations

n, k = map(int,input().strip().split())
arr = combinations(sorted(set(input().split()), key = int),int(k))
# print(arr)
print('\n'.join([' '.join(x) for x in arr]))
# 8 3
# 2 4 4 3 5 1 3 4