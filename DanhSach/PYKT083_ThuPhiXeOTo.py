def cost(loaixe, soghe):
    if loaixe == 'Xe_con' and soghe == '5': return 10000
    if loaixe == 'Xe_con' and soghe == '7': return 15000
    if loaixe == 'Xe_tai' and soghe == '2': return 20000
    if loaixe == 'Xe_khach' and soghe == '29': return 50000
    return 70000
n = int(input())
ListCost = {}
for _ in range(n):
    inp = input().split()
    if inp[3] == 'OUT': continue
    ListCost[inp[4]] = ListCost.get(inp[4], 0) + cost(inp[1], inp[2])

for i in ListCost.keys():
    print(f'{i}: {ListCost[i]}')


# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021