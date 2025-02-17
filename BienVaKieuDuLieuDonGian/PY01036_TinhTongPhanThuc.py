for t in range(int(input())):
    number = int(input())
    sum = float(0)
    if number%2 == 0:
        for i in range(2,number+2,2):
            sum += (1/i)
    else:
        for i in range(1,number+2,2):
            sum += (1/i)
    print(f'{sum:.6f}')