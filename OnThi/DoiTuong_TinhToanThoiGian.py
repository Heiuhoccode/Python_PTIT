from datetime import datetime


class gamer:
    def __init__(self,id, name, inp, outp):
        self.id = id
        self.name = name
        self.inp = datetime.strptime(inp, "%H:%M")
        self.outp = datetime.strptime(outp, "%H:%M")
    def times(self):
        a = self.outp - self.inp
        return a

    def __str__(self):
        gio = int(self.times().total_seconds()//3600)
        phut = int((self.times().total_seconds()-gio*3600)//60)
        return f'{self.id} {self.name} {gio} gio {phut} phut'


n = int(input())
dsgm = []
for _ in range(n):
    dsgm.append(gamer(input(), input(), input(), input()))
dsgm = sorted(dsgm, key=lambda x: -x.times())
for i in dsgm:
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