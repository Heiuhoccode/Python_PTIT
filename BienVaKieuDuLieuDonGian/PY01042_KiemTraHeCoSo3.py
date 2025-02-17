for t in range(int(input())):
    number = input()
    if(number.count('0') + number.count('1') + number.count('2') == len(number)):
        print("YES")
    else:
        print("NO")