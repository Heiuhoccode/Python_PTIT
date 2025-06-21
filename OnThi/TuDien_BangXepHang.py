ds = []

for _ in range(int(input())):
    dic = {}
    name = input()
    ac, sub = map(int,input().split())
    dic['name'] = name
    dic['ac'] = ac
    dic['sub'] = sub
    ds.append(dic)
ds = sorted(ds, key=lambda x: (-x['ac'], x['sub'], x['name']))
for i in ds:
    print(f'{i["name"]} {i["ac"]} {i["sub"]}')
# 2
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 168 600