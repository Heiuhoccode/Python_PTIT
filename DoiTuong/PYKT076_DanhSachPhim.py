from datetime import datetime
class CategoryFilm:
    def __init__(self, id, name):
        self.id = "TL" + format(id,"03d")
        self.name = name
    def getId(self):
        return self.id
    def getName(self):
        return self.name
class Film:
    def __init__(self, id, idCa, date, name, episodeNum):
        self.id = "P" + format(id,"03d")
        self.idCa = idCa
        self.nameCa = ""
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.date1 = date
        self.name = name
        self.episodeNum = episodeNum

    def getIdCa(self):
        return self.idCa
    def setNameCategory(self, nameCa):
        self.nameCa = nameCa
    def __str__(self):
        return f'{self.id} {self.nameCa} {self.date1} {self.name} {self.episodeNum}'
ListCategory = []
ListFilm = []
n,m = map(int,input().split())
for i in range(n):
    ListCategory.append(CategoryFilm(i+1, input()))
for i in range(m):
    ListFilm.append(Film(i+1, input(), input(), input(), int(input())))
for i in range(n):
    for j in range(m):
        if ListCategory[i].getId() == ListFilm[j].getIdCa():
            ListFilm[j].setNameCategory(ListCategory[i].getName())
ListFilm = sorted(ListFilm,key=lambda x: (x.date, x.name, -x.episodeNum))
for i in ListFilm:
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