def check(number):
    for i in range(len(number)-1):
        if(number[i] > number[i+1]):
            return False
    return True
for i in range(int(input())):
    number = input()
    if(check(number)):
        print("YES")
    else:
        print("NO")
