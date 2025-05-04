from itertools import count


# def check(arr):
#     for i in range(len(arr)-1):
#         if arr.count(i) !=1:
#             return "NO"
#     return "YES"
# for t in range(int(input())):
#     n = int(input())
#     arr = []
#     for i in map(int,input().strip().split()):
#         arr.append(i)
#     print(check(arr))


arr = []
n = int(input())
for i in range(n):
    arr.append(input())
def turn