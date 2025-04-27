from sympy import Matrix


class Validation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.determinant = None
        self.square_matrix = []
        self.b_matrix = []
        self.validate_error = None
        self.valid = self.validate()

    def validate(self):
        if self.matrix[1] == 0:
            self.validate_error = "ERROR file: something wrong with matrix"
            return False
        try:
            mtrx_var_qty = self.matrix[1]
            mtrx_height = len(self.matrix[0])
            if mtrx_height != mtrx_var_qty:
                self.validate_error = "difference between variables end equality numbers"
                return False
            for row in self.matrix[0]:
                if len(row) - 1 != mtrx_var_qty:
                    self.validate_error = "wrong number of coefficients"
                    return False
        except Exception as e:
            print(e)
            self.validate_error = e
            return False
        return True

    def get_square_matrix(self):
        for row in self.matrix[0]:
            self.square_matrix.append(row[:-1])
            self.b_matrix.append(row[-1:])

    def get_determinant(self):
        if self.determinant:
            return self.determinant
        if not self.square_matrix:
            self.get_square_matrix()
        self.determinant = Matrix(self.square_matrix).det()
        return self.determinant

    @staticmethod
    def obtain_determinant(square_mtrx):
        return Matrix(square_mtrx).det()

    def _validate_cramer(self):
        if 0 < self.matrix[1] < 5:
            return True
        else:
            return False

    def validate_methods(self):
        res = {
            'determinant': self.determinant if self.determinant else self.get_determinant(),
            'cramer': False,
            'gauss': False,
            'gauss_jordan': False
        }
        if self.determinant != 0:
            res['cramer'] = self._validate_cramer()
            res['gauss'] = True
            res['gauss_jordan'] = True
        return res
