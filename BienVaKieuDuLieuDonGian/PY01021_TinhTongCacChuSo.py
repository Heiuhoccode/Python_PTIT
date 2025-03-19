def change(s):
    sum = 0
    arr = []
    for i in s:
        if 'A' <= i <= 'Z':
            arr.append(i)
        else:
            sum += int(i)
    arr.sort()
    new_s = ""
    for i in arr:
        new_s += i
    return f"{new_s}{sum}"
for t in range(int(input())):
    s = input()
    print(change(s))