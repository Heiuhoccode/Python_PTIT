from unicodedata import decimal

file = open("DATA.in", "r")
List = []
for i in file:
    for j in i.split():
        if not (j.isdecimal() and int(j) < 2**31):
            List.append(j)
List = sorted(List)
for i in List:
    print(i, end=' ')