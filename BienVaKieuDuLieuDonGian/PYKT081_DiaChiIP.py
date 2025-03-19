def check(arr):
    if len(arr) != 4:
        return "NO"
    for i in arr:
        if i  > 255 or i < 0:
            return "NO"
    return "YES"
for t in range(int(input())):
    try:
        arr = list(map(int, input().strip().split(".")))
        print(check(arr))
    except: print("NO")
# 2
# 192.168.1.1
# 256.255.255.255