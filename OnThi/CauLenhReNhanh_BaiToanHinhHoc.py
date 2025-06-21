# import math
#
#
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# def kc(p1,p2):
#     return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
#
# for _ in range(int(input())):
#     dsp = []
#     n = int(input())
#     k = int(input())
#     for _ in range(n):
#         x,y=map(int,input().split())
#         dsp.append(point(x,y))
#     end = False
#     for i in range(len(dsp)-2):
#         if end == True: break
#         for j in range(i+1,len(dsp)-1):
#             if end == True: break
#             for u in range(j+1, len(dsp)):
#                 if end == True: break
#                 x1, y1 = dsp[i].x, dsp[i].y
#                 x2, y2 = dsp[j].x, dsp[j].y
#                 x3, y3 = dsp[u].x, dsp[u].y
#                 # print(f'A({x1},{y1}), B({x2},{y2}), C({x3},{y3})')
#                 D = 2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
#                 # print(f'D={D}')
#                 EPS=1e-6
#                 if abs(D) < EPS: continue
#                 x = (x1**2+y1**2)*(y2-y3) + (x2**2+y2**2)*(y3-y1) + (x3**2+y3**2)*(y1-y2)
#                 x /= D
#                 y = (x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3) + (x3 ** 2 + y3 ** 2) * (x2 - x1)
#                 y /= D
#                 I = point(x,y)
#                 R = kc(dsp[u],I)
#                 # print("R =",R)
#                 cnt = 0
#                 for m in dsp:
#                     khoangcach = kc(m,I)
#                     # print(khoangcach)
#                     if 0<khoangcach < R-EPS:
#                         cnt += 1
#                 if cnt == k:
#                     print("YES")
#                     end = True
#                     break
#     if end == False:
#         print("NO")
# # 2
# # 4
# # 1
# # 0 0
# # 5 0
# # 0 5
# # 1 1
# # 5
# # 2
# # 5 5
# # 5 -5
# # -5 5
# # -5 -5
# # 0 0
for i in range(150):
    print(i)