from datetime import *
class VDV:
    def __init__(self, name, dvi, finish):
        self.id = self.process(name,dvi)
        self.name = name
        self.dvi = dvi
        self.finish = datetime.strptime(finish,"%H:%M")
    def process(self,name,dvi):
        names = name.split()
        dvis = dvi.split()
        id = ""
        for i in dvis:
            id = id + i[0].upper()
        for i in names:
            id = id + i[0].upper()

        return id
    def thoigian(self):
        start = datetime.strptime("6:00", "%H:%M")
        timee = self.finish - start
        timee = timee.seconds/3600
        return timee
    def vantoc(self):
        timee = self.thoigian()
        return int(round(120/timee,0))
    def __str__(self):
        return f'{self.id} {self.name} {self.dvi} {self.vantoc()} Km/h'

ListVDV = []
for _ in range(int(input())):
    ListVDV.append(VDV(input(),input(),input()))
ListVDV = sorted(ListVDV, key=lambda x: x.thoigian())
for i in ListVDV:
    print(i)

# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45