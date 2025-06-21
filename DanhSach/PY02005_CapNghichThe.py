n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j] < a[i]: cnt +=1
print(cnt)
# 5
# 2 4 1 3 5