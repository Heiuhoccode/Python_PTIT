import sys


class Rectangle:
    def __init__(self, a, b, colorr):
        self.a = a
        self.b = b
        self.colorr = colorr.strip()
    def perimeter(self):
        return (self.a+self.b)*2
    def area(self):
        return self.a * self.b
    def color(self):
        newColor = str(self.colorr[0]).upper() + str(self.colorr[1:]).lower()
        return newColor

arr = input().split()
if not (int(arr[0]) > 0 and int(arr[1]) > 0):
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
sys.exit()
if __name__ == '__main__':
    arr = input().split()
    try:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    except:
        print("INVALID")