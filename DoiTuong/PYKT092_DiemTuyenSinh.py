class Candidate:
    def __init__(self, id, name, score, nation, region):
        self.id = "TS" + format(id, "02d")
        self.name = self.change(name)
        self.score = score
        self.nation = nation
        self.region = region
        self.status = self.setStatus()

    def change(self,name):
        names = name.strip().split()
        res = ""
        for i in names:
            i = i.lower()
            res = res + str(i[0]).upper() + i[1:] + " "
        res = res.strip()
        return res
    def totalScore(self):
        scoreMajority = 0
        if self.region == 1: scoreMajority += 1.5
        elif self.region == 2: scoreMajority += 1
        elif self.region == 3: scoreMajority += 0

        if self.nation == "Kinh": scoreMajority += 0
        else: scoreMajority += 1.5
        return self.score + scoreMajority

    def setStatus(self):
        if self.totalScore() >= 20.5: return "Do"
        return "Truot"
    def __str__(self):
        return f'{self.id} {self.name} {self.totalScore()} {self.status}'

ListCandidate = []
for i in range(int(input())):
    ListCandidate.append(Candidate(i+1, input(), float(input()), input(), int(input())))
ListCandidate = sorted(ListCandidate, key=lambda x: (-x.totalScore(), x.id))
for i in ListCandidate:
    print(i)

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3