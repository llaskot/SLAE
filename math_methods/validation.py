from sympy import Matrix
from math_methods.jacobi import Jacobi


class Validation:
    jacobi_order = None

    def __init__(self, matrix):
        Validation.jacobi_order = None
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

    def _validate_jacobi(self):
        """
        checks diagonal dominance and variables number
        set static variable jacobi_order in order to jacobi method order
        :return: Bool
        """
        res = {}
        if 0 < self.matrix[1] <= 20:
            if not self.square_matrix:
                self.get_square_matrix()
            matr = (Jacobi.convert_matrix((self.square_matrix, self.matrix[1])))[0]
            for i in range(len(matr)):
                temp = [abs(x) for x in matr[i]]
                max_value = max(temp)
                x_ind = [i for i, x in enumerate(temp) if x == max_value]
                if len(x_ind) != 1:
                    return False
                if (sum(temp) - max_value) >= max_value:
                    return False
                res[i] = x_ind[0]
            if len(set(res[x] for x in res.keys())) != self.matrix[1]:
                return False
            Validation.jacobi_order = res
            return True

    def validate_methods(self):
        res = {
            'determinant': self.determinant if self.determinant else self.get_determinant(),
            'cramer': False,
            'gauss': False,
            'gauss_jordan': False,
            'jacoby': False
        }
        if self.determinant != 0:
            res['cramer'] = self._validate_cramer()
            res['gauss'] = True
            res['gauss_jordan'] = True
            res['jacoby'] = self._validate_jacobi()
        return res
