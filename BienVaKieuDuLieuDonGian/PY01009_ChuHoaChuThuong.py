stringg = input()
count = 0
for i in range(len(stringg)):
    if(stringg[i].isupper()):
        count += 1
if(count > len(stringg)/2):
    print(stringg.upper())
else:
    print(stringg.lower())