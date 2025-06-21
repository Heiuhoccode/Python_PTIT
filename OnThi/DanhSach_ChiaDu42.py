n = 0
a = []
while n<10:
    temp = list(map(int,input().split()))
    n += len(temp)
    a += temp
cnt=0
b = set()
for i in a:
    b.add(i%42)
print(len(b))