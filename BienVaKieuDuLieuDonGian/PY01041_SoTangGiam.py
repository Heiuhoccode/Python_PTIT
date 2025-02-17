def check(n):
    if(len(n) < 3):
        return False
    max = '0'
    for i in n:
        if(max < i):
            max = i
    for i in range(0,n.find(max)):
        if n[i] >= n[i+1]:
            return False
    for i in range(n.find(max)+1,len(n)):
        if n[i-1] <= n[i]:
            return False
    return True
for t in range(int(input())):
    number = input()
    if check(number):
        print("YES")
    else:
        print("NO")

