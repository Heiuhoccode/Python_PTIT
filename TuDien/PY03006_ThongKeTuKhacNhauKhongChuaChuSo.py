import re
listTu = []
tu = {}
for i in range(int(input())):
    s = re.sub(r'[^a-zA-Z\s]',' ',input()).split()
    for j in s:
        j = j.lower()
        tu[j] = tu.get(j,0) + 1
    tuMoi = sorted(tu.keys(), key=lambda x: (-tu[x], x))
for key in tuMoi:
    print(f'{key} {tu[key]}')
# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi/ dich benh xuat hien PTIT trich hon 6 ty :dong ho tro sinh vien PTIT
# voi muc ho . tro, 500000? dong/sinh vien P;TIT.