listSub = []
for i in range(int(input())):
    subject = {}
    id = input()
    name = input()
    exam = input()
    subject["id"] = id
    subject["name"] = name
    subject["exam"] = exam
    listSub.append(subject)
listSub = sorted(listSub, key=lambda x: x["id"])
for i in listSub:
    print(f'{i["id"]} {i["name"]} {i["exam"]}')

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen