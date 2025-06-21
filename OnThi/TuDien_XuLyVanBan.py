import re
def change(s):
    res = ""
    temps = s.lower().split()
    if not temps:
        return ""
    a = temps[0]
    res += str(a[0]).upper() + a[1:] + " "
    res += ' '.join(temps[1:])
    return res
s = ""
while True:
    try:
        temp = input()
        s += temp
    except: break

cau = re.split('[.?!]',s)
for i in cau:
    print(change(i))

# ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
#     vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.