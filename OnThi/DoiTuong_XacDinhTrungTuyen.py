MU = {}
MU["A"]="TOAN"
MU['B']="LY"
MU['C']="HOA"
MU['1']=2.0
MU['2']=1.5
MU['3']=1.0
MU['4']=0.0
class GV:
    def __init__(self, id, name, mon_uutien, tin, chuyen):
        self.id = "GV" + format(id, "02d")
        self.name = name
        self.mon = MU[mon_uutien[0]]
        self.uutien = MU[mon_uutien[1]]
        self.tin = tin
        self.chuyen = chuyen
    def tong(self):
        return self.tin*2 + self.chuyen + self.uutien
    def rank(self):
        if self.tong() >= 18: return "TRUNG TUYEN"
        return "LOAI"
    def __str__(self):
        return f'{self.id} {self.name} {self.mon} {self.tong()} {self.rank()}'

n = int(input())
dsgv = []
for i in range(n):
    dsgv.append(GV(i+1, input(), input(), float(input()), float(input())))
dsgv = sorted(dsgv, key=lambda x: -x.tong())
for i in dsgv:
    print(i)

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0