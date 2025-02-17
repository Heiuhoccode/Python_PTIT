for t in range(int(input())):
    number = input()
    tich = 1
    for i in number:
        if i != '0':
            tich *= (ord(i)-48)
    print(tich)
