import copy

from .gauss import Gauss
from .validation import Validation


class Cramer(Gauss):
    def __init__(self, matrix: (list[list], int), validation):
        super().__init__(matrix)
        # self.vld = Validation(matrix)
        self.vld = validation
        self.a_matrix = self.vld.square_matrix
        self.b_matrix = self.vld.b_matrix
        self.determinant = self.vld.get_determinant()
        self.determinants = []

    def get_result(self):
        for i in range(self.length):
            temp = copy.deepcopy(self.a_matrix)
            for j in range(self.length):
                temp[j][i] = self.b_matrix[j][0]
            self.determinants.append(self.vld.obtain_determinant(temp))
            self.result[i + 1] = self.determinants[i] / self.determinant

    def show_process(self):
        d = f'Determinant:\nD = {self.determinant}\nCramer’s minors:\n'
        cd = [f'D[X{i+1}] = {self.determinants[i]}' for i in range(self.length)]
        return d + '\n'.join(cd)
