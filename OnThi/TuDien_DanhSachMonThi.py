ds = []
for _ in range(int(input())):
    dic={}
    dic["id"] = input()
    dic["name"] = input()
    dic["exam"] = input()
    ds.append(dic)
ds = sorted(ds, key=lambda x: x["id"])
for i in ds:
    print(f'{i["id"]} {i["name"]} {i["exam"]}')
# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen