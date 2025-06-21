from re import search


class person:
    def __init__(self,name,tel, date):
        self.name = name
        self.tel = tel
        self.date = date[5:]
    def __str__(self):
        return f'{self.name}: {self.tel} {self.date}'
listperson = []
data = []
try:
    with open("SOTAY.txt", "r") as file:
        data = file.readlines()
except:
    print("LOI FILE")
data = [line.strip() for line in data]
i=0
for i in range(len(data)):
    datee = ""
    if search("Ngay", data[i]):
        datee = data[i]
        for j in range(i+1, len(data),2):
            if search("Ngay", data[j]):
                i=j
                break
            else:
                name = data[j]
                tel = data[j+1]
                listperson.append(person(name,tel,datee))

try:
    with open("DIENTHOAI.txt", "w") as file1:
        for i in listperson:
            file1.write(f'{i}\n')
except:
    print("LOI FILE")