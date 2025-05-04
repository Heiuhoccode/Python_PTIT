from datetime import *
class Client:
    def __init__(self,id , name, room, checkin, checkout, addFee):
        self.id = "KH" + format(id,"02d")
        self.name = name
        self.room = room
        self.checkin = datetime.strptime(checkin,"%d/%m/%Y")
        self.checkout = datetime.strptime(checkout,"%d/%m/%Y")
        self.addFee = addFee

    def dateStay(self):
        dateStay = self.checkout - self.checkin
        return dateStay.days + 1

    def totalPayment(self):
        price = 0
        if self.room//100 == 1: price = 25
        elif self.room//100 == 2: price = 34
        elif self.room//100 == 3: price = 50
        else: price = 80
        return price*self.dateStay() + self.addFee

    def __str__(self):
        return f'{self.id} {self.name} {self.room} {self.dateStay()} {self.totalPayment()}'

ListClient = []
for i in range(int(input())):
    ListClient.append(Client(i+1,input(), int(input()), input().strip(), input().strip(), int(input())))
ListClient = sorted(ListClient,key=lambda x: -x.totalPayment())
for i in ListClient:
    print(i)
# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96