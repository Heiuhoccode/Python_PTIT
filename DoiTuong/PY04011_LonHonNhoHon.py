# class Compare:
#     def __init__(self, compare):
#         self.left = compare.split()[0]
#         self.right = compare.split()[2]
#         self.compare = compare.split()[1]
#         self.status = self.getStatus()
#
#     def getStatus(self):
#         if self.compare == "<": return "Nho Hon"
#         return "Lon Hon"
#     def __str__(self):
#         if self.status == "Lon Hon":
#             return f'{self.left} {self.status} {self.right}'
#         return f'{self.left} {self.status} {self.right}'
#
# ListCompare = []
# for _ in range(int(input())):
#     ListCompare.append(Compare(input()))
# DirectoryCompare = {}
# for i in ListCompare:
#
#
# # 3
# # An > Binh
# # Binh > Cong
# # An < Cong