test = int(input())
for i in range(test):
    number = input()
    if (number.count("4") + number.count("7")) == len(number):
        print("YES")
    else:
        print("NO")