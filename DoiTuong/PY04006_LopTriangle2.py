import math


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self, p1):
        return math.sqrt(math.pow((self.x-p1.x),2)+math.pow((self.y-p1.y),2))

class Triangle:
    def __init__(self, AB, BC, AC):
        self.AB = AB
        self.BC = BC
        self.AC = AC

    def area(self):
        return 0.25*math.sqrt((self.AC + self.AB + self.BC)*(self.AC - self.AB + self.BC)*(self.AC + self.AB - self.BC)*(self.AB - self.AC + self.BC))

for _ in range(int(input())):
    x1,y1,x2,y2,x3,y3 = map(float, input().split())
    A = Point(x1,y1)
    B = Point(x2,y2)
    C = Point(x3,y3)

    AB = A.distance(B)
    BC = B.distance(C)
    AC = A.distance(C)
    if AB + BC <= AC or AB + AC <= BC or AC + BC <= AB:
        print("INVALID")
    else:
        triangle = Triangle(AB,BC,AC)
        print(f'{round(triangle.area(),2):.{2}f}')
# ==Input==
# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0

# ==Output==
#INVALID
#INVALID
#17.071