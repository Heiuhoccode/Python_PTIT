test = int(input())

for i in range(test):
    number = input()
    if(len(number)<2):
        print(number)
    else:
        newNumber = ""
        temp = int(number[len(number)-1])
        for i in range(len(number)-1):

            temp1 = int(number[len(number) - 2 - i])
            if(temp >= 5):
                temp1+=1
            temp = 0
            newNumber = newNumber[1:]
            newNumber = str(temp) + newNumber
            if(temp1==10 and i!=len(number)-2):
                newNumber = str(0) + newNumber
            else:
                newNumber = str(temp1) + newNumber
            temp = temp1
        print(newNumber)


"""
7
15
14
5
99
12345678
44444445
1445

"""
