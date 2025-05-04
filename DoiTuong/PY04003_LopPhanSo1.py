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
    def __str__(self):
        return f'{self.tu}/{self.mau}'

tu,  mau = map(int, input().split())
p1 = PhanSo(tu,mau)
p1 = p1.rutgon()
print(p1)