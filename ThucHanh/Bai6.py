from datetime import datetime
class CaThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = ma
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.time = datetime.strptime(ngay + ' ' + gio, '%d/%m/%Y %H:%M')

arr = []
file = open('CATHI.in', 'r')
cnt = 0
for i in range(int(file.readline())):
    cnt += 1
    arr.append(CaThi(cnt,file.readline().strip(), file.readline().strip(), file.readline().strip()))
arr = sorted(arr, key=lambda x: (x.time, x.ma))

for i in arr:
    a="C"
    if(i.ma<100):a=a+"0"
    if(i.ma<10): a=a+"0"
    print(a,end="")
    print(i.ma,i.ngay,i.gio,i.phong)