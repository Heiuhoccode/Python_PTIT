n = int(input())
a = sorted(list(map(float,input().split())))
for i in range(1,len(a)-1):
    if a[i]==a[0] or a[i]==a[len(a)-1]: a[i]=0
a[0], a[len(a)-1]=0,0
sum,cnt = 0,0
for i in a:
    if i != 0:
        cnt+=1
    sum += i
print(round(sum/cnt,2))
# 6
# 6.75 8 9.2 7.25 7.75 6.75