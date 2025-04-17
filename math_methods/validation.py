from sympy import Matrix


class Validation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.determinant = None
        self.square_matrix = []
        self.valid

    def validate(self):
        mtrx_var_qty = self.matrix[1]
        mtrx_height = len(self.matrix[0])
        if mtrx_height != mtrx_var_qty:
            return False
        d



    def get_square_matrix(self):
        for row in self.matrix[0]:
            self.square_matrix.append(row[:-1])

    def get_determinant(self):
        self.determinant = Matrix(self.square_matrix).det()
        return self.determinant




