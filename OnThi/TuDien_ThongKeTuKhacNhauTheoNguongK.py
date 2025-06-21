import re
dic = {}
n,k = map(int, input().split())
for _ in range(n):
    s = re.sub(r'[^\w\s]',' ', input()).split()
    for i in s:
        i = i.lower()
        dic[i] = dic.get(i,0) + 1
ds = sorted(dic.keys(), key=lambda x: [-dic[x],x])
for i in ds:
    if dic[i] >= k:
        print(f'{i} {dic[i]}')


# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.