vertex,edge,point = map(int, input().split())
dsCanh = [[] for x in range(0,vertex+1)]
for i in range(edge):
    vertex1, vertex2 = map(int, input().split())
    dsCanh[vertex1].append(vertex2)
    dsCanh[vertex2].append(vertex1)
chuaxet = [0]*(vertex+1)
hangdoi = [point]
chuaxet[point] = 1
while(len(hangdoi) > 0):
    temp = hangdoi.pop()
    for i in dsCanh[temp]:
        if chuaxet[i] == 0:
            hangdoi.append(i)
            chuaxet[i] = 1
check = True
for i in range(1,vertex+1):
    if chuaxet[i] == 0:
        check = False
        print(i)
if check: print(0)


# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5