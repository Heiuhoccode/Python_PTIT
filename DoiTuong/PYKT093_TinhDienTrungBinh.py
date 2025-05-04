from decimal import Decimal, ROUND_HALF_UP


class Student:
    def __init__(self, id, name, score1, score2, score3):
        self.id = "SV" + format(id, "02d")
        self.name = self.change(name)
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.avgScore = self.setAvgScore()
        self.rank = 0

    def change(self, name):
        names = name.strip().split()
        res = ""
        for i in names:
            i = i.lower()
            res = res + str(i[0]).upper() + i[1:] + " "
        res = res.strip()
        return res

    def setAvgScore(self):
        avgScore = (self.score1 * 3 + self.score2 * 3 + self.score3 * 2) / 8
        value = Decimal(str(avgScore))
        res = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return res

    def updateRank(self, rank):
        self.rank = rank
    def getRank(self): return self.rank
    def __str__(self):
        return f'{self.id} {self.name} {round(self.avgScore,2)} {self.rank}'

ListStudent = []
for i in range(int(input())):
    ListStudent.append(Student(i+1, input(), float(input()), float(input()), float(input())))
ListStudent = sorted(ListStudent, key=lambda x: (-x.avgScore, x.id))
ListStudent[0].updateRank(1)
for i in range(1, len(ListStudent)):
    if ListStudent[i].avgScore == ListStudent[i-1].avgScore:
        ListStudent[i].updateRank(ListStudent[i-1].getRank())
    else:
        ListStudent[i].updateRank(i+1)
for i in ListStudent:
    print(i)
# 4
# ha   Thi    kieu    anh
# 7
# 6
# 7
# ha   Thi    kieu    anh
# 7
# 6
# 7
# ha   Thi    kieu    anh
# 7
# 6
# 7
# Pham       THi       HAO
# 6
# 7
# 6