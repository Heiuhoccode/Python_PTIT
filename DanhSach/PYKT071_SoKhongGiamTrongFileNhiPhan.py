import pickle
def notDecrease(a):
    a = str(a)
    if len(a) == 1: return False
    for i in range(1,len(a)):
        if a[i-1] > a[i]: return False
    return True
res1 = {}
res2 = {}
try:
    with open("DATA1.in","rb") as file:
        a = pickle.load(file)
    for i in a:
        if notDecrease(i):
            res1[i] = res1.get(i, 0) + 1
except:
    print("DATA1.in hong")
try:
    with open("DATA2.in","rb") as file:
        a = pickle.load(file)
    for i in a:
        if notDecrease(i):
            res2[i] = res2.get(i, 0) + 1
except:
    print("DATA2.in hong")
keys = sorted(res1.keys())
for i in keys:
    if i in res2.keys():
        print(f'{i} {res1[i]} {res2[i]}')