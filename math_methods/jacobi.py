from math_methods.gauss import Gauss





class Jacobi(Gauss):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.matrix = convert_matrix(matrix)

    def convert_matrix(self, matrix):
        pa