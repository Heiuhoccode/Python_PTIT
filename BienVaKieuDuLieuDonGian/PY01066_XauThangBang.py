def check(u,u1):
    for i in range(1,len(n)):
        a,b,c,d = ord(n[i-1]),ord(n[i]),ord(n1[i-1]),ord(n1[i])
        if(abs(a-b) != abs(c-d)):
            return False
    return True
for t in range(int(input())):
    n = input()
    n1 = n[::-1]
    if check(n,n1):
        print("YES")
    else:
        print("NO")
