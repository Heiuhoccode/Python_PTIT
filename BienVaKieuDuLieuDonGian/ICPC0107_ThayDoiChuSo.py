def change(s,x,y):
    new_s = ""
    for i in range(len(s)):
        if s[i] == y:
            new_s += x
        else:
            new_s += s[i]
    return new_s
def min_max(p,q,x1,x2):
    min_sum = int(change(x1,p,q)) + int(change(x2,p,q))
    max_sum = int(change(x1,q,p)) + int(change(x2,q,p))
    return f"{min_sum} {max_sum}"
for t  in range(int(input())):
    p,q = [int(i) for i in input().split()]
    if p > q:
        p,q = q,p
    x1 = input()
    if len(x1.split()) > 1: x1,x2 = x1.split()
    else: x2 = input()
    print(min_max(str(p),str(q),x1,x2))