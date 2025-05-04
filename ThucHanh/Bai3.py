
file = open("CONTACT.in")
arr = []
for i in file:
    s = i.strip().lower()
    if s not in arr:
        arr.append(s)
arr=sorted(arr)
for i in arr:
    print(i)