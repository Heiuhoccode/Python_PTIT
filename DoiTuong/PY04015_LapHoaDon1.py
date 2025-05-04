class Client:
    def __init__(self, id, name, oldIndex, newIndex):
        self.id = "KH" + format(id,'02d')
        self.name = name
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.total = self.calculateFee()

    def calculateFee(self):
        index = self.newIndex - self.oldIndex
        if index <= 50:
            return index*100*1.02
        if index <= 100:
            return (50*100 + (index-50)*150)*1.03
        return (50*100 + 50*150 + (index-100)*200)*1.05

    def __str__(self):
        return f'{self.id} {self.name} {self.total:.0f}'

listClient = []
for t in range(int(input())):
    name = input()
    oldIndex = int(input())
    newIndex = int(input())
    listClient.append(Client(t+1,name,oldIndex,newIndex))
listClient = sorted(listClient, key=lambda x: (-x.total,x.id))
for i in listClient:
    print(i)
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612