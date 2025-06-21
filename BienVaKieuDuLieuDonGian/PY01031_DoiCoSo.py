from string import digits


def binToB(heSo, num):
    res = ""
    digist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num > 0:
        res = digist[num%heSo] + res
        num //= heSo
    return res

for _ in range(int(input())):
    num, heSo = map(int,input().split())
    # print(f'{heSo} {bin}')
    print(binToB(heSo,num))