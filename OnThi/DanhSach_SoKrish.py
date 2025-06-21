def giaithua(a):
    if a==0 or a==1: return 1
    return a*giaithua(a-1)
def check(s):
    sum = 0
    for i in s:
        sum+=giaithua(int(i))
    if sum == int(s): return "Yes"
    return "No"
for _ in range(int(input())):
    print(check(input()))