n = input()[::-1]
res = ""
cnt=0
for i in n:
    if cnt==3:
        res += "," + i
        cnt = 1
    else:
        res += i
        cnt += 1
print(res[::-1])