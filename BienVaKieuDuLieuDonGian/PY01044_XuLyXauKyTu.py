a = input().lower().split()
b = input().lower().split()
hop,giao = [],[]
for i in a:
    if i not in giao and i in b:
        giao.append(i)
    if i not in hop: hop.append(i)
for i in b:
    if i not in hop: hop.append(i)

hop = sorted(hop)
giao = sorted(giao)

for i in hop:
    print(i, end=' ')
print()
for i in giao:
    print(i, end=' ')

# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++