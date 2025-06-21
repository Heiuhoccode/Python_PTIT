from datetime import datetime
class theloai:
    def __init__(self,id, name):
        self.id = "TL" + format(id, "03d")
        self.name = name

class phim:
    def __init__(self,id,idTL,dat, name,sotap ):
        self.id = "P" + format(id, "03d")
        self.idTl = idTL
        self.dat = datetime.strptime(dat, "%d/%m/%Y")
        self.name = name
        self.sotap = sotap
        self.theloai = ""
    def setTL(self, tl):
        self.theloai = tl
    def __str__(self):
        return f'{self.id} {self.theloai} {self.dat.strftime("%d/%m/%Y")} {self.name} {self.sotap}'

n,m = map(int,input().split())
dstl,dsph = [],[]
for i in range(n):
    dstl.append(theloai(i+1,input()))
for i in range(m):
    dsph.append(phim(i+1, input(), input(), input(), int(input())))
for i in dstl:
    for j in dsph:
        if i.id == j.idTl:
            j.setTL(i.name)
dsph = sorted(dsph, key=lambda x: [x.dat, x.name, -x.sotap])
for i in dsph:
    print(i)

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5