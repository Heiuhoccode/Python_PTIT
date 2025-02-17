def check(s):
    sum = 0
    for i in s:
        sum += ord(i) - 48
    sum = str(sum)
    # print(sum)
    if(sum == sum[::-1] and len(sum) > 1):
        return True
    return False
for t in range(int(input())):
    # check(input())
    if check(input()):
        print("YES")
    else:
        print("NO")
