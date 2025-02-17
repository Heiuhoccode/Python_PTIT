p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    res=""
    inp = input()
    if(inp == '0'):
        break
    k, s = inp.split()
    k = int(k)
    for i in s:
        res = p[(p.find(i)+k)%28] + res
    print(res)
