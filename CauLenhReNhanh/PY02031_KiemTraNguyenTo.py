import math


def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True
def change(A,n,m):
    B = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if isPrime(A[i][j]):
                B[i][j] = 1
    return B
n,m = map(int, input().split())
A = []
for i in range(n):
    B = list(map(int,input().split()))
    A.append(B)
newA = change(A,n,m)
for i in newA:
    for j in i:
        print(j, end = ' ')
    print()

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9