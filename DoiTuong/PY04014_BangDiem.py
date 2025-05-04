from decimal import Decimal, ROUND_HALF_UP


class HocSinh:
    def __init__(self, id, name, avgScore):
        self.id = "HS" + format(id,'02d')
        self.name = name
        self.avgScore = avgScore
        self.rank = self.rankUpdate()

    def rankUpdate(self):
        if self.avgScore >= 9: return "XUAT SAC"
        if 8 <= self.avgScore: return "GIOI"
        if 7 <= self.avgScore: return "KHA"
        if 5 <= self.avgScore: return "TB"
        return "YEU"

    def __str__(self):
        return self.id+" "+self.name+" "+str(self.avgScore.quantize(Decimal('0.1'),rounding=ROUND_HALF_UP))+" "+self.rank

dshs = []
for i in range(int(input())):
    name = input()
    scores = list(map(Decimal,input().split()))
    avgScore = Decimal(scores[0])*2 + Decimal(scores[1])*2
    for j in range(2,len(scores)):
        avgScore += Decimal(scores[j])
    avgScore /= 12
    dshs.append(HocSinh(i+1,name,avgScore))
dshs = sorted(dshs, key=lambda x: (-x.avgScore,x.id))
for i in dshs:
    print(i)

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0