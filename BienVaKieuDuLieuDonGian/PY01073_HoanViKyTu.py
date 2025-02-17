from itertools import permutations

s = input()
for i in list(permutations(s)):
    temp = ""
    for u in i:
        temp += str(u)
    print(temp)