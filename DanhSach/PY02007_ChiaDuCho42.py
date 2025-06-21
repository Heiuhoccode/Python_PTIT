a={}
while True:
    try:
        s = input()
        if s == '':continue
        for i in s.split():
            a[int(i)%42] = 1
    except: break
print(len(a))
# 42 84 252 420 840
# 126 42 84 420 126