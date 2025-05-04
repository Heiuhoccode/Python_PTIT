
class tu:
    def __init__(self,s,cnt):
        self.s = s
        self.cnt = cnt
    def __str__(self):
        return f'{self.s} {self.cnt}'
n = int(input())
arr = []
s = ""
while n>0:
    s += input().lower() + " "
    n -= 1
a = ""
for i in range(len(s)):
    if s[i]==',' or s[i]=='.' or s[i]=='?' or s[i]=='!' or s[i]==':' or s[i]==';' or s[i]=='-' or s[i]=='/':
        a += " "
    else:
        a += s[i]
arr_tu =[]
for i in a.split():
    if i not in arr:
        arr.append(i)
        temp = tu(i,a.count(i))
        arr_tu.append(temp)
for i in sorted(arr_tu, key=lambda x: (-x.cnt, x.s)):
    print(i)

# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.