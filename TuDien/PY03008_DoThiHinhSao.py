temp = {}
def check():
    for i in temp:
        if temp[i]==len(temp)-1: return "Yes"
    return "No"
for i in range(int(input())-1):
    a,b=map(int,input().split())
    temp[a] = temp.get(a,0) + 1
    temp[b] = temp.get(b, 0) + 1
print(check())
