for i in range(int(input())):
    number = input()

    dau = number[0] + number[1]
    cuoi = number[len(number)-2] + number[len(number)-1]
    if(dau == cuoi):
        print("YES")
    else:
        print("NO")