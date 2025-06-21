n = int(input())
temp=1
arr = sorted(list(map(int,input().split())))
for i in range(1,len(arr)):
    if arr[i]-arr[i-1] != 1:
        temp=0
        print(arr[i-1]+1)
        break
if temp==1:
    print(arr[len(arr)-1] + 1)