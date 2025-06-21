import re
def change(s):
    temp = s.lower().split()
    if not temp:
        return ""
    a = ""
    a += temp[0][0].upper() + temp[0][1:]
    for i in temp[1:]:
        a += " " + i
    return a
temp = ""
while True:
    try:
        s = input()
        if s == '':continue
        temp += s
    except: break
# temp = input()
a = re.split('[.?!]', temp)
for i in a:
    print(change(i))

# ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.