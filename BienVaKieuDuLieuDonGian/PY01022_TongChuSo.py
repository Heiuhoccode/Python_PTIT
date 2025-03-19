def tong(s):
    if len(s) == 1: return 0
    sum = 0
    for i in s:
        sum += ord(i)-48
    return 1 + tong(str(sum))
n = input()
if len(n) <= 1: print(1)
else: print(tong(n))
