n = input()
a = list(map(int,input().split()))
sum = 0
for i in range(0,len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]: sum +=1
print(sum)