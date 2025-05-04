class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self, Com):
        a = self.a + Com.a
        b = self.b + Com.b
        return Complex(a,b)
    def multiply(self,Com):
        a = self.a * Com.a + (-1)*self.b*Com.b
        b = self.a*Com.b + self.b*Com.a
        return Complex(a,b)
    def __str__(self):
        if self.b < 0:
            return f'{self.a} - {(-1)*self.b}i'
        return f'{self.a} + {self.b}i'

for _ in range(int(input())):
    a1,b1,a2,b2 = map(int, input().split())
    Com1 = Complex(a1,b1)
    Com2 = Complex(a2,b2)
    C = (Com1.sum(Com2)).multiply(Com1)
    D = (Com1.sum(Com2)).multiply(Com1.sum(Com2))
    print(f'{C}, {D}')

# 3
# 1 2 3 4
# 2 3 4 5
# 1 -2 5 -6