import re
doc = ''
i = 100
while i>0:
    i -= 1
    try:
        doc += input()
        if doc[-1] not in '.?!': doc+=' .'
        else:
            if doc[-2] != ' ': doc = f'{doc[:-1]} {doc[-1]}'
        doc += ' '
    except:
        break
words = re.split(r'(?<=[.?!])\s+', doc)
for e in words:
    x = ' '.join(e.split()).lower()
    x=x.capitalize()
    a=x.split()
    for i in range (len(a)):
        if(i!=len(a)-2):
            print(a[i],end=" ")
        else: print(a[i],end="")
    print()