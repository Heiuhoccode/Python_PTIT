n,m,x = map(int,input().split())
check = [True for _ in range(n)]
check[x-1] = False
g=[]
for i in range(m):
    temp = list(map(int,input().split()))
    g.append(temp)
k = True
while k:
    k=False
    for i in g:
        if check[i[0]-1] == False and check[i[1]-1]==True:
            check[i[1]-1] = False
            k=True
        elif check[i[0]-1] == True and check[i[1]-1]==False:
            check[i[0]-1] = False
            k=True
for i in range(len(check)):
    if check[i] == True:
        print(i+1)
# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5