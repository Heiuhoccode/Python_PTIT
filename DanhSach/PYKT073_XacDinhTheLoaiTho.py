n = int(input())
b=[]
for _ in range(n):
    b.append(len(input().split()))
i=0
res = ""
while i < len(b):
    l8 = False
    while b[i]==6 or b[i]==8:
        if i < len(b)-1: i += 1
        else: break
        l8 = True
    if l8:
        res += '1'
        l8 = False
    tntt = False
    cnt=0
    while b[i]==7:
        if i < len(b) -1: i+=1
        else: break
        cnt+=1
        tntt=True
    if tntt:
        for _ in range(cnt//4):
            res += '2'
        tntt = False
    if i < len(b):
        i += 1
print(len(res))
for i in res:
    print(i)

# 16
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon