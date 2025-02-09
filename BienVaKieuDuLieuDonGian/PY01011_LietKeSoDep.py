
def check(u):
    if(u != u[::-1] or len(u)%2!=0 ):
        return False
    for i in u:
        if(int(i)%2!=0):
            return False
    return True


for i in range(int(input())):
    for u in range(22, int(input()), 2):
        if (check(str(u))):
            print(u, end=' ')
    print()