from datetime import datetime
class MonHoc:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def getId(self): return self.id
    def getName(self): return self.name

class LichThi:
    def __init__(self,id, idMonHoc, date, time, group):
        self.id = "T" + format(id, "03d")
        self.idMonHoc = idMonHoc
        self.date = datetime.strptime(date,"%d/%m/%Y")
        self.date1 = date
        self.time = datetime.strptime(time,"%H:%M")
        self.time1 = time
        self.group = group
        self.name = ""
    def getIdMonHoc(self): return self.idMonHoc
    def setName(self,name):
        self.name = name
    def __str__(self):
        return f"{self.id} {self.idMonHoc} {self.name} {self.date1} {self.time1} {self.group}"

ListMonHoc = []
ListLichThi = []
n,m = map(int,input().split())
for i in range(n):
    ListMonHoc.append(MonHoc(input(), input()))
for i in range(m):
    idMonHoc, date, time, group = input().split()
    ListLichThi.append(LichThi(i+1, idMonHoc, date, time, group))

for i in range(n):
    for j in range(m):
        if ListMonHoc[i].getId() == ListLichThi[j].getIdMonHoc():
            ListLichThi[j].setName(ListMonHoc[i].getName())

ListLichThi = sorted(ListLichThi, key=lambda x: (x.date, x.time, x.idMonHoc))
for i in ListLichThi:
    print(i)

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05