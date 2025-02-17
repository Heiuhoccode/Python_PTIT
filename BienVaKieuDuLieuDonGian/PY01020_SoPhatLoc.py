for t in range(int(input())):
    number = input()
    res = ""
    res = res  + number[len(number)-2]+ number[len(number)-1]
    if(res == "86"):
        print("YES")
    else:
        print("NO")