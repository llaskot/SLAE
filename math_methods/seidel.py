from copy import copy

from math_methods.jacobi import Jacobi


class Seidel(Jacobi):
    def __init__(self, matrix):
        super().__init__(matrix)

    def formula(self):
        new_x = copy(self.x)
        for i in range(self.length):
            new_x[i] = (1 / self.converted_matrix[i][i]) * (self.converted_matrix[i][-1] - self.get_s_left(i, new_x))
        self.check_diff(new_x)
        self.x = new_x

    def get_s_left(self, row_num, new_x):
        res = 0
        for i in range(self.length):
            if i == row_num:
                continue
            res += self.converted_matrix[row_num][i] * new_x[i]
        return res
