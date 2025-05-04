class Candidate:
    def __init__(self, id, name, theoryScore, praticeScore):
        self.id = "TS0" + str(id)
        self.name = name
        if(theoryScore > 10): theoryScore /= 10
        self.theoryScore = theoryScore
        if(praticeScore > 10): praticeScore /= 10
        self.practiceScore = praticeScore
        self.avgScore = (self.theoryScore + self.practiceScore) / 2
        self.status = self.setStatus()

    def setStatus(self):
        if self.avgScore < 5: return "TRUOT"
        if self.avgScore < 8: return "CAN NHAC"
        if self.avgScore <= 9.5: return "DAT"
        return "XUAT SAC"

    def __str__(self):
        return f'{self.id} {self.name} {self.avgScore:.2f} {self.status}'

listCandidate = []
for i in range(int(input())):
    name = input()
    theoryScore = float(input())
    practiceScore = float(input())
    listCandidate.append(Candidate(i+1,name,theoryScore,practiceScore))
listCandidate = sorted(listCandidate, key=lambda x: -x.avgScore)
for i in listCandidate:
    print(i)

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56