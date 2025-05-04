
class Matrix:
    def __init__(self, n,m,matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def transfer(self):
        matrix_m2 = []
        for i in range(self.m):
            temp = []
            for j in range(self.n):
                temp.append(self.matrix[j][i])
            matrix_m2.append(temp)
        return matrix_m2
    def transfer_matrix(self):
        n = self.m
        m = self.n
        matrix = self.transfer()
        return Matrix(n,m,matrix)
    def multiply(self, M2):
        matrix_m3 = [[0 for _ in range(M2.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(M2.m):
                for k in range(self.m):
                    matrix_m3[i][j] += self.matrix[i][k] * M2.matrix[k][j]
        return matrix_m3
        # return numpy.dot(self.matrix, M2.matrix)

for _ in range(int(input())):
    n,m = map(int,input().split())
    matrix = []
    for i in range(n):
        temp = list(map(int,input().split()))
        matrix.append(temp)

    M1 = Matrix(n,m,matrix)
    M2 = M1.transfer_matrix()
    result = M1.multiply(M2)
    for i in result:
        for j in i:
            print(j, end = ' ')
        print()

# 1
# 2  2
# 1  2
# 3  4