
for i in range(int(input())):
    encode = input()
    newNumber = ""
    for i1 in range(0,len(encode)-1,2):
        temp = encode[i1]
        cnt = int(encode[i1+1])
        for u in range(cnt):
            newNumber = newNumber + temp
    print(newNumber)