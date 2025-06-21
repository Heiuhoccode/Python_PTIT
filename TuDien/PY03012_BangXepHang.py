
dssv = []
for i in range(int(input())):
    sinhvien = {}
    name = input()
    ac, submit = map(int,input().split())
    sinhvien["name"]= name
    sinhvien["ac"]= ac
    sinhvien["submit"]=submit
    dssv.append(sinhvien)
dssv = sorted(dssv, key=lambda x:(-x["ac"],x["submit"],x["name"]))
for i in dssv:
    print(f'{i["name"]} {i["ac"]} {i["submit"]}')

# 2
# C
# 168 600
# B
# 168 500