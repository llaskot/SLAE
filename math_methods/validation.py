from sympy import Matrix


class Validation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.determinant = None
        self.square_matrix = []


    def get_square_matrix(self):
        for row in self.matrix[0]:
            self.square_matrix.append(row[:-1])

    def get_determinant(self):
        self.determinant = Matrix(self.square_matrix).det()
        return self.determinant




