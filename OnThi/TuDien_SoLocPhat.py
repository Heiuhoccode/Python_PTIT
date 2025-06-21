for _ in range(int(input())):
    n = int(input())
    s = ""
    if n < 8: print(0)
    else:
        for i in range(8,n+1,8):
            s += str(i)
        print(s.count('6') + s.count('8'))