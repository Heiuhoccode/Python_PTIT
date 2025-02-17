def tong(u):
    sum = 0
    for i in range(1, len(u), 2):
        sum += ord(u[i])-48
    return sum

def tich(u):
    nhan = 1
    for i in range(0,len(u), 2):
        if u[i]!='0':
            nhan *= (ord(u[i])-48)
    return nhan

for t in range(int(input())):
    number = input()
    print(tich(number), tong(number))
# 3
# 12345678
# 20000
# 22334455667788