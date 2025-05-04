from datetime import datetime


class Gamer:
    def __init__(self, id, name, start, end):
        self.id = id
        self.name = name
        self.start = datetime.strptime(start, "%H:%M")
        self.end = datetime.strptime(end, "%H:%M")
        self.timee, self.times = self.CalculateTime()

    def CalculateTime(self):
        time = self.end -  self.start
        gio = time.total_seconds()//3600
        phut = (time.total_seconds() - gio*3600)//60
        return f"{int(gio)} gio {int(phut)} phut", time.total_seconds()

    def __str__(self):
        return f'{self.id} {self.name} {self.timee}'

ListGamer = []
for _ in range(int(input())):
    ListGamer.append(Gamer(input(),input(),input(),input()))
ListGamer = sorted(ListGamer, key=lambda x: -x.times)
for i in ListGamer:
    print(i)

# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00