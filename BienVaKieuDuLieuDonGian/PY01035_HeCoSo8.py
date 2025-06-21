def binToB(heSo, bin):
    decimalNum = int(bin,2)
    res = ""
    digist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while decimalNum > 0:
        res = digist[decimalNum%heSo] + res
        decimalNum //= heSo
    return res
bin = input()
print(binToB(8,bin))