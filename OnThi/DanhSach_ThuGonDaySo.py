n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    if len(b) == 0 or (i+b[-1])%2!=0:
        b.append(i)
    else:
        b.pop(-1)
print(len(b))
# a=[0,1,2,3,4,5]
# print(a[:2])
# print(a[4:])