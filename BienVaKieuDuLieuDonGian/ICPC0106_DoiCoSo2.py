def doicoso(thapphan, coso):
    res = ""
    p = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while thapphan > 0:
        res = p[thapphan%coso] + res
        thapphan //= coso
    return res
for t in range(int(input())):
    coso = int(input())
    binary = input()
    if coso == 2: print(binary)
    else:
        thapphan = int(binary,2)
        print(doicoso(thapphan, coso))
# 2
# 8
# 10010100010010101
# 2
# 10010100010010101