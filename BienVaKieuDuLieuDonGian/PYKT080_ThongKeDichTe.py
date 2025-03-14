def analys(arr,row,column):
    sum =0
    for i in range(row):
        for u in range(column):
            if arr[i][u] == -1:
                arr[i][u] = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if(x==0 and y==0): continue
                        if i+x >=0 and u+y >=0 and i+x<=row-1 and u+y<=column-1 and arr[i+x][u+y]>=0:
                            sum += arr[i+x][u+y]
                            arr[i+x][u+y] = 0
    return sum
row, column = map(int,input().strip().split())
arr = []
for i in range(row):
    arr.append(list(map(int,input().strip().split())))
print(analys(arr,row,column))