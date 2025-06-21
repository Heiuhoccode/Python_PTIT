def exitt(a):
    for i in a:
        if i != 0: return False
    return True
def equall(a):
    for i in range(1,len(a)):
        if a[i-1] != a[i]: return False
    return True
def change(a):
    b=[0 for i in range(4)]
    for i in range(len(a)-1):
        b[i] = abs(a[i]-a[i+1])
    b[3] = abs(a[3]-a[0])
    return b
a = []
while True:
    a = list(map(int, input().split()))
    if exitt(a): break
    cnt = 0
    while not equall(a):
        a = change(a)
        cnt += 1
    print(cnt)
