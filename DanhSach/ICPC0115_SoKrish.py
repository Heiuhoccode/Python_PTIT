def giaithua(n):
    if n==1 or n==0: return 1
    return n*giaithua(n-1)
def check(n):
    sum = 0
    for i in str(n):
        sum += giaithua(int(i))
    if n == sum: return "Yes"
    return "No"
for _ in range(int(input())):
    n = int(input())
    print(check(n))