import math
import sys

ds = []
with open("DATA.in","r") as f:
    for f1 in f.readlines():
        s = f1.split()
        for i in s:
            if i.isdecimal() and int(i) < 2**31: continue
            else: ds.append(i)
ds = sorted(ds)
for i in ds:
    print(i,end=' ')