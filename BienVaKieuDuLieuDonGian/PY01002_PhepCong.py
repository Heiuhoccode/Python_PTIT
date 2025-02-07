bieuThuc = input()
temp = bieuThuc.split()
soHang1,phepCong,soHang2,phepGan,tong = temp
soHang1,soHang2,tong = int(soHang1),int(soHang2),int(tong)
if soHang1 + soHang2 == tong:
    print("YES")
else:
    print("NO")