from datetime import datetime

class monhoc:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class lichthi:
    def __init__(self, id, idM, dat, gio, team):
        self.id = "T" + format(id, "03d")
        self.idM = idM
        self.dat = datetime.strptime(dat, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.team = team
        self.name = ""

    def setName(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id} {self.idM} {self.name} {self.dat.strftime("%d/%m/%Y")} {self.gio.strftime("%H:%M")} {self.team}'

n,m = map(int,input().split())
dsmh, dslt = [],[]
for i in range(n):
    dsmh.append(monhoc(input(), input()))
for i in range(m):
    idM, dat, gio, team = map(str, input().split())
    dslt.append(lichthi(i+1,idM,dat,gio,team))
for i in dslt:
    for j in dsmh:
        if i.idM == j.id:
            i.setName(j.name)
            break
dslt = sorted(dslt, key=lambda x: [x.dat, x.gio, x.idM])
for i in dslt:
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