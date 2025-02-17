def change(u):
    return u+int(str(u)[::-1])
for t in range(int(input())):
    cnt = 1000
    number = int(input())
    while(number%7!=0 and cnt > 0 ):
        number = change(number)
        cnt -= 1
    if(number%7==0):
        print(number)
    if cnt ==0:
        print(-1)