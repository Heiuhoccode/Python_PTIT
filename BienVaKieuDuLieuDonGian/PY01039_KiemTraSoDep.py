def check(u):
    temp = u[0]
    temp1 = u[1]
    for i in range(0,len(u),2):
        if(temp != u[i]):
            return False
    for i in range(1, len(u), 2):
        if (temp1 != u[i]):
            return False
    return True
for t in range(int(input())):
    if(check(input())):
        print("YES")
    else:
        print("NO")