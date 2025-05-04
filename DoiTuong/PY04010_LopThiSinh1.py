class ThiSinh:
    def __init__(self, name, dob, score1, score2, score3):
        self.name = name
        self.dob = dob
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.sumScore = score1 + score2 + score3

    def __str__(self):
        return f'{self.name} {self.dob} {self.sumScore:.1f}'

name = input()
dob = input()
score1 = float(input())
score2 = float(input())
score3 = float(input())
TS = ThiSinh(name,dob,score1,score2,score3)
print(TS)

# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5