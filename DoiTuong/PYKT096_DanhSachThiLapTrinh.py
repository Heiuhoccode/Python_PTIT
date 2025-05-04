
class Team:
    def __init__(self, id, nameTeam, nameSchool):
        self.id = "Team" + format(id,"02d")
        self.nameTeam = nameTeam
        self.nameSchool = nameSchool
    def getId(self): return self.id
    def __str__(self):
        return f'{self.nameTeam} {self.nameSchool}'
class ThiSinh:
    def __init__(self, id, name, idTeam):
        self.id = "C" + format(id, "03d")
        self.name = name
        self.idTeam = idTeam

    def getIdTeam(self): return self.idTeam
    def __str__(self):
        return f'{self.id} {self.name}'

ListTeam = []
for i in range(int(input())):
    ListTeam.append(Team(i+1, input().strip(), input().strip()))
ListThiSinh = []
for i in range(int(input())):
    ListThiSinh.append(ThiSinh(i+1, input().strip(), input().strip()))
ListThiSinh = sorted(ListThiSinh, key=lambda x: x.name)
for i in ListThiSinh:
    for j in ListTeam:
        if i.getIdTeam() == j.getId():
            print(f'{i} {j}')

# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02