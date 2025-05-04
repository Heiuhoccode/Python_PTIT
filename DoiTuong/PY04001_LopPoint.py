import math


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self, p1):
        return math.sqrt(math.pow((self.x-p1.x),2)+math.pow((self.y-p1.y),2))

for _ in range(int(input())):
    x1, y1, x2, y2 = map(float, input().split())
    P1 = Point(x1,y1)
    P2 = Point(x2,y2)
    print(f'{P1.distance(P2):.{4}f}')

# 2
# 0 0 0 5
# 0 199 5 6