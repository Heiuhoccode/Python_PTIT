from string import digits


def binToB(heSo, bin):
    decimalNum = int(bin,2)
    res = ""
    digist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while decimalNum > 0:
        res = digist[decimalNum%heSo] + res
        decimalNum //= heSo
    return res
with open("DATA.in", 'r') as file:
    for _ in range(int(file.readline())):
        heSo = int(file.readline())
        bin = file.readline()
        # print(f'{heSo} {bin}')
        print(binToB(heSo,bin))