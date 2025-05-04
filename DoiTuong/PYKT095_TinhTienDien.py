class HoGiaDinh:
    def __init__(self, id, ten, loai, chisoDau, chisoCuoi):
        self.id = "KH" + format(id, "02d")
        self.ten = self.change(ten)
        self.loai = loai
        self.chisoDau = chisoDau
        self.chisoCuoi = chisoCuoi

    def change(self, name):
        names = name.strip().split()
        res = ""
        for i in names:
            i = i.lower()
            res = res + str(i[0]).upper() + i[1:] + " "
        res = res.strip()
        return res
    def tienTrongDM(self):
        if self.loai == "A":
            if (self.chisoCuoi - self.chisoDau) <= 100:
                return (self.chisoCuoi - self.chisoDau)*450
            return 100*450
        elif self.loai == "B":
            if (self.chisoCuoi - self.chisoDau) <= 500:
                return (self.chisoCuoi - self.chisoDau)*450
            return 500*450
        elif self.loai == "C":
            if (self.chisoCuoi - self.chisoDau) <= 200:
                return (self.chisoCuoi - self.chisoDau)*450
            return 200*450
    def tienNgoaiDM(self):
        if self.loai == "A" and (self.chisoCuoi - self.chisoDau) > 100:
            return (self.chisoCuoi - self.chisoDau -100)*1000
        elif self.loai == "B" and (self.chisoCuoi - self.chisoDau) > 500:
            return (self.chisoCuoi - self.chisoDau - 500)*1000
        elif self.loai == "C" and (self.chisoCuoi - self.chisoDau) > 200:
            return (self.chisoCuoi - self.chisoDau - 200)*1000
        return 0
    def VAT(self):
        return self.tienNgoaiDM()/20
    def tongTien(self):
        return self.tienTrongDM() + self.tienNgoaiDM() + self.VAT()
    def __str__(self):
        return f'{self.id} {self.ten} {self.tienTrongDM()} {self.tienNgoaiDM()} {self.VAT():.0f} {self.tongTien():.0f}'

ListHoGiaDinh = []
for i in range(int(input())):
    id = i+1
    ten = input()
    inp= input().split()
    loai = inp[0].strip()
    chisoDau = int(inp[1].strip())
    chisoCuoi = int(inp[2].strip())
    ListHoGiaDinh.append(HoGiaDinh(id, ten,loai, chisoDau, chisoCuoi))
ListHoGiaDinh = sorted(ListHoGiaDinh,key=lambda x: -x.tongTien())
for i in ListHoGiaDinh:
    print(i)
# 2
#  nGuyEn Hong Ngat
# C 200 278
#  Chu thi    minh
# A 120 160