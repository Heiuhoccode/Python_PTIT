class Expert:
    def __init__(self, id, name, idExam, scoreTech, scoreExpert):
        self.id = "GV" + format(id,"02d")
        self.name = name
        self.idExam = idExam
        self.scoreTech = scoreTech
        self.scoreExpert = scoreExpert
        self.status = self.setStatus()

    def getExamMajority(self):
        examD = {}
        examD["A"] = "TOAN"
        examD["B"] = "LY"
        examD["C"] = "HOA"
        exam = examD[self.idExam[0]]
        majority = 0
        if self.idExam[1] == "1": majority = 2
        elif self.idExam[1] == "2": majority = 1.5
        elif self.idExam[1] == "3":majority = 1
        elif self.idExam[1] == "4":majority = 0

        return exam, majority

    def getTotalScore(self):
        exam, majority = self.getExamMajority()
        return (self.scoreTech*2 + self.scoreExpert) + majority

    def setStatus(self):
        if self.getTotalScore() >= 18: return "TRUNG TUYEN"
        return "LOAI"

    def __str__(self):
        exam, majority = self.getExamMajority()
        return f'{self.id} {self.name} {exam} {self.getTotalScore()} {self.status}'

ListExpert = []
for i in range(int(input())):
    ListExpert.append(Expert(i+1,input(), input(), float(input()), float(input())))
ListExpert = sorted(ListExpert, key=lambda x: -x.getTotalScore())
for i in ListExpert:
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
