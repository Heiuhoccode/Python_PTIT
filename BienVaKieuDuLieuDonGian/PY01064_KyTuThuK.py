def genS(i, S):
    digist = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    left,right = S, S
    mid = digist[i]
    return left + mid + right
for _ in range(int(input())):
    n, k = map(int, input().split())
    S = ""
    for i in range(1,n+1):
        S = genS(i,S)
    print(S[k-1])