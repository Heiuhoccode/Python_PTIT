class Staff:
    def __init__(self, id, name, wage, workDay):
        self.id = id
        self.name = name
        self.wage = wage
        self.workDay = workDay
        self.group = self.setGroup()
        self.department = self.setDepartment(department)
        self.seniority = self.setSeniority()
    def setGroup(self):
        return self.id[0]
    def setSeniority(self):
        seniority = self.id[1] + self.id[2]
        return int(seniority)
    def getDepartment(self):
        return self.id[3] + self.id[4]
    def setDepartment(self, department):
        self.department = department
    def totalWage(self):
        multip = 1
        if self.group == "A":
            if 1 <= self.seniority <=3: multip = 10
            elif 4 <= self.seniority <= 8: multip = 12
            elif 9 <= self.seniority <= 15: multip = 14
            else: multip = 20
        elif self.group == "B":
            if 1 <= self.seniority <=3: multip = 10
            elif 4 <= self.seniority <= 8: multip = 11
            elif 9 <= self.seniority <= 15: multip = 13
            else: multip = 16
        elif self.group == "C":
            if 1 <= self.seniority <=3: multip = 9
            elif 4 <= self.seniority <= 8: multip = 10
            elif 9 <= self.seniority <= 15: multip = 12
            else: multip = 14
        else:
            if 1 <= self.seniority <=3: multip = 8
            elif 4 <= self.seniority <= 8: multip = 9
            elif 9 <= self.seniority <= 15: multip = 11
            else: multip = 13
        return self.wage*self.workDay*multip
    def __str__(self):
        return f'{self.id} {self.name} {self.department} {self.totalWage()*1000}'
Department = {}
for i in range(int(input())):
    inp = input().split()
    idDe = inp[0]
    department = ""
    for j in range(1,len(inp)):
        department += inp[j] +" "
    Department[idDe] = department.strip()
ListStaff = []
for i in range(int(input())):
    ListStaff.append(Staff(input(), input(), int(input()), int(input())))
for i in ListStaff:
    i.setDepartment(Department[i.getDepartment()])
    print(i)

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24