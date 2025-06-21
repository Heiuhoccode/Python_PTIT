for _ in range(int(input())):
    n = int(input())
    tuDien = {}
    for _ in range(n):
        a = int(input())
        tuDien[a] = tuDien.get(a,1) + 1
    tu = sorted(tuDien.keys(), key=lambda x: (-tuDien[x], x))
    print(tu[0])

# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13