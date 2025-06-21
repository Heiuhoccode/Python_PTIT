from ctypes.wintypes import PPOINT


class NV:
    def __init__(self, id, name, wage, days):
        self.id = id
        self.name = name
        self.wage = wage
        self.days = days
        self.phongban = id[3:]
    def setPhongBan(self,pb):
        self.phongban = pb
    def LuongThang(self):
        hsn = 1
        nhom = self.id[0]
        namLV = int(self.id[1:3])
        if nhom == 'A':
            if 1 <= namLV <= 3:
                hsn = 10
            elif 4 <= namLV <= 8:
                hsn = 12
            elif 9 <= namLV <= 15:
                hsn = 14
            else:
                hsn = 20
        elif nhom == 'B':
            if 1 <= namLV <= 3:
                hsn = 10
            elif 4 <= namLV <= 8:
                hsn = 11
            elif 9 <= namLV <= 15:
                hsn = 13
            else:
                hsn = 16
        elif nhom == 'C':
            if 1 <= namLV <= 3:
                hsn = 9
            elif 4 <= namLV <= 8:
                hsn = 10
            elif 9 <= namLV <= 15:
                hsn = 12
            else:
                hsn = 14
        else:
            if 1 <= namLV <= 3:
                hsn = 8
            elif 4 <= namLV <= 8:
                hsn = 9
            elif 9 <= namLV <= 15:
                hsn = 11
            else:
                hsn = 13
        return self.wage * self.days * hsn * 1000

    def __str__(self):
        return f'{self.id} {self.name} {self.phongban} {self.LuongThang()}'

n = int(input())
PhongBan = {}
for _ in range(n):
    inp = input().split()
    a = inp[0]
    b = ' '.join(inp[1:])
    PhongBan[a.strip()]=b.strip()
n = int(input())
dsnv = []
for _ in range(n):
    dsnv.append(NV(input(), input(), int(input()), int(input())))
for i in dsnv:
    i.setPhongBan(PhongBan[i.phongban])
    print(i)

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24

