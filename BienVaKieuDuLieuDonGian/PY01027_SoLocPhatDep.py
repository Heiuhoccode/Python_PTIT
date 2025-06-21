s= input() + "1"
i=0
while(0 <= s.find('688') < len(s)-3):
    a = s[0:s.find('688')] + s[s.find('688')+3:len(s)]
    s = a
    # print(a)
while(0 <= s.find('68') < len(s)-2):
    a = s[0:s.find('68')] + s[s.find('68')+2:len(s)]
    s = a
    # print(a)
while(0 <= s.find('6') < len(s)-1):
    a = s[0:s.find('6')] + s[s.find('6')+1:len(s)]
    s = a
    # print(a)
if s == "1": print("YES")
else: print("NO")

# s = input()
# i = 0
# n = len(s)
# valid = True
#
# while i < n:
#     if i + 2 < n and s[i:i+3] == "688":
#         i += 3
#     elif i + 1 < n and s[i:i+2] == "68":
#         i += 2
#     elif s[i] == "6":
#         i += 1
#     else:
#         valid = False
#         break
#
# print("YES" if valid else "NO")