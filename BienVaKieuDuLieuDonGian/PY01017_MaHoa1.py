for t in range(int(input())):
    number = input() + "."
    count = 0
    res=""
    temp = number[0]
    for i in number:
        if temp == i:
            count += 1
        else:
            res = res + str(count) + temp
            temp = i
            count = 1

    print(res)
