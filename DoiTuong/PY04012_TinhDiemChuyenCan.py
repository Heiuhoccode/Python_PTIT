class SinhVien:
    def __init__(self,id, name, clas):
        self.id = id
        self.name = name
        self.clas = clas
        self.score = 10
        self.status = "DDK"

    def getId(self): return self.id
    def updateScore(self, status):
        score = 10
        for i in status:
            if i == 'm': score -= 1
            elif i == 'v': score -= 2
        if score <= 0:
            self.score = 0
            self.status = "KDDK"
        else:
            self.score = score
    def __str__(self):
        if self.status == "KDDK":
            return f'{self.id} {self.name} {self.clas} {self.score} {self.status}'
        return f'{self.id} {self.name} {self.clas} {self.score}'

ListStudent = []
cnt = int(input())
for _ in range(cnt):
    ListStudent.append(SinhVien(input(),input(),input()))
for _ in range(cnt):
    # print(input())
    id, status = input().strip().split()
    for i in ListStudent:
        if id == i.getId():
            i.updateScore(status)
for i in ListStudent:
    print(i)
# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm