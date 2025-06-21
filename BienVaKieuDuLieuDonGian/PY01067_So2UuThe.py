
for _ in range(int(input())):
    n = int(input())
    for i in range(100000):
        if n < 1: break
        if str(i).count('2') > len(str(i))//2 and str(i).count('2')+str(i).count('1')+str(i).count('0') == len(str(i)):
            print(i, end=' ')
            n -= 1

    print()