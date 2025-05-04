class HoaDon:
    def __init__(self, mmh, tenmh, soluong, dongia, chietkhau):
        self.mmh = mmh
        self.tenmh = tenmh
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tong = soluong * dongia - chietkhau
HoaDons = []
for t in range(int(input())):
    HoaDons.append(HoaDon(input(),input(),int(input()),int(input()),int(input())))
HoaDons = sorted(HoaDons,key=lambda x:(-x.tong))
for i in HoaDons:
    print(i.mmh, i.tenmh, i.soluong, i.dongia, i.chietkhau, i.tong)

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