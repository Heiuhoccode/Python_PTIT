# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# hop, AtruB, BtruA = [],[],[]
# for i in a:
#     if i in a and i in b and i not in hop:
#         hop.append(i)
#
# for i in a:
#     if i in a and i not in b and i not in AtruB:
#         AtruB.append(i)
#
# for i in b:
#     if i not in a and i in b and i not in BtruA:
#         BtruA.append(i)
# hop=sorted(hop)
# AtruB=sorted(AtruB)
# BtruA=sorted(BtruA)
# for i in hop:
#     print(i, end=' ')
# print()
# for i in AtruB:
#     print(i, end=' ')
# print()
# for i in BtruA:
#     print(i, end=' ')
# # 5 6
# # 1 2 3 4 5
# # 3 4 5 6 7 8
print(pow(8,15,23))