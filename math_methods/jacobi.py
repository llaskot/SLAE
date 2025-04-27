from math_methods.gauss import Gauss





class Jacobi(Gauss):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.matrix = self.convert_matrix(matrix)

    def convert_matrix(self, matrix):
        for i in range(len(matrix[0])):
            matrix[0][i] = [float(val) for val in matrix[0][i]]
        print(matrix)
        return matrix
