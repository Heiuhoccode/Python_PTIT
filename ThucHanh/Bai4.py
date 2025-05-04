def doicoso(thapphan, coso):
    res = ""
    # s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # for i in range(coso):
    #     p += s[i]
    while thapphan > 0:
        res = p[thapphan%coso] + res
        thapphan //= coso
    return res

a,b,m = map(int,input().split())
cnt=0
for i in range(a,b+1,1):
    for k in range(2,m+1,1):
        temp = doicoso(i,k)
        if(temp == temp[::-1]):
            print(temp)
            cnt += 1
print(cnt)