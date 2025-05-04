import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        ucln = math.gcd(self.tu, self.mau)
        tu = self.tu // ucln
        mau = self.mau // ucln
        return PhanSo(tu,mau)
    def tong(self, p2):
        tong_mau = self.mau * p2.mau // math.gcd(self.mau, p2.mau)
        tong_tu = self.tu * (tong_mau//self.mau) + p2.tu * (tong_mau//p2.mau)
        return PhanSo(tong_tu,tong_mau)
    def __str__(self):
        return f'{self.tu}/{self.mau}'

tu1, mau1, tu2, mau2 = map(int, input().split())
p1 = PhanSo(tu1,mau1).rutgon()
p2 = PhanSo(tu2,mau2).rutgon()
print(p1.tong(p2))