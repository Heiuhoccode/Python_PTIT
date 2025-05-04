class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = str(color[0]).upper() + str(color[1:]).lower()
        self.perimeter = (length+width)*2
        self.area = length*width
    def __str__(self):
        return f'{self.perimeter} {self.area} {self.color}'


inp = input().split()
length, width, color = int(inp[0]), int(inp[1]), inp[2]
if length > 0 and width > 0:
    R = Rectangle(length, width, color)
    print(R)
else:
    print("INVALID")


