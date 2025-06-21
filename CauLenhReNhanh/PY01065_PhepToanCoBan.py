def check(so1, so2, so3, dau):
    if dau == '+': return so1+so2==so3
    if dau == '-': return so1 - so2 == so3
    if dau == '*': return so1 * so2 == so3
    if so2 == 0: return False
    if so1%so2 == 0: return so1 // so2 == so3
    return False

def change(a):
    ans = []
    if a[0] == '?' and a[1] != '?':
        for i in range(1,10):
            ans.append(str(i) + a[1])
    elif a[1] == '?' and a[0] != '?':
        for i in range(0,10):
            num = a[0] + str(i)
            if int(num) >= 10:  # Đảm bảo số >= 10
                ans.append(num)
    elif a[0] == '?' and a[1] == '?':
        for i in range(1,10):
            for j in range(0,10):
                ans.append(str(i) + str(j))
    else:
        if 10 <= int(a) <=99: ans.append(a)
    return ans
def change_dau(a):
    if a == '?': return ['+', '-', '*', '/']
    return [a]
def process():
    temp  = 0
    pheptoan = input()
    thanhphan = pheptoan.split()
    if len(thanhphan) != 5:  # Kiểm tra định dạng
        print("WRONG PROBLEM!")
        return
    so1 = change(thanhphan[0])
    so2 = change(thanhphan[2])
    so3 = change(thanhphan[4])
    dau = change_dau(thanhphan[1])
    for a in so1:
        for option in dau:
            for b in so2:
                for c in so3:
                    if (check(int(a), int(b), int(c), option)):
                        print(f'{a} {option} {b} = {c}')
                        return
    print("WRONG PROBLEM!")
for i in range(int(input())):
    process()
