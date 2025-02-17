def check(u):
    sum = ord(u[0])-48
    for i in range(1,len(u)):
        sum += ord(u[i])-48
        if(abs(ord(u[i-1]) - ord(u[i])) != 2):
            return False
    if(sum%10!=0):
        return False
    return True
for t in range(int(input())):
    if check(input()):
        print("YES")
    else:
        print("NO")
