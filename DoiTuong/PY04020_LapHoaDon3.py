class Bill:
    def __init__(self, id, name, quantity, price, discount):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount

    def getTotalPayment(self):
        return self.quantity*self.price - self.discount

    def __str__(self):
        return f"{self.id} {self.name} {self.quantity} {self.price} {self.discount} {self.getTotalPayment()}"

ListBill = []
for i in range(int(input())):
    ListBill.append(Bill(input(), input(), int(input()), int(input()), int(input())))
ListBill = sorted(ListBill, key=lambda x: -x.getTotalPayment())
for i in ListBill:
    print(i)

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000