def change(s):
    pos = 0
    full0 = True
    for i in range(len(s)):
        if s[i]!='0':
            pos = i
            full0 =False
            break
    if full0: return '0'
    return s[pos:]

def equall(a):
    for i in range(1,len(a)):
        if a[i-1] != a[i]: return False
    return True
while True:
    n = int(input())
    if n == 0: break;
    a = []
    for i in range(n):
        a.append(change(input()))
    a = sorted(a, key=lambda x: (len(x), x))
    if equall(a): print("BANG NHAU")
    else: print(f'{a[0]} {a[len(a)-1]}')
    print()

# 5
# 1
# 2
# 3
# 4
# 5
# 3
# 001
# 22
# 33333333333333333333333333333333333
# 3
# 1
# 1
# 1
# 0