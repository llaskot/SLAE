from fractions import Fraction
import copy


class Gauss:
    def __init__(self, matrix: (list[list], int)):
        self.matrix = matrix[0]
        self.length = matrix[1]
        self.temp_row: list = []
        self.converted_matrix = copy.deepcopy(self.matrix)
        self.result = {}

    def get_coefficient(self, row, index, ) -> Fraction:
        # print(self.matrix)
        return -1 * self.converted_matrix[row][index] / self.converted_matrix[index][index]

    def get_temp_row(self, coeff, row):
        self.temp_row = [x * coeff for x in self.converted_matrix[row]]

    def update_matrix(self):
        for i in range(1, self.length):
            for j in range(i):
                if self.converted_matrix[i][j] == 0:
                    continue
                if self.converted_matrix[i - 1][j] == 0 and i - 1 == j:
                    self.converted_matrix[i], self.converted_matrix[i - 1] = \
                        self.converted_matrix[i - 1], self.converted_matrix[i]
                    continue
                coef = self.get_coefficient(i, j)
                self.get_temp_row(coef, j)
                self.converted_matrix[i] = [x + y for x, y in zip(self.converted_matrix[i], self.temp_row)]

    def get_result(self):
        solution = {}
        i = self.length
        while i > 0:
            last = self.converted_matrix.pop()
            res = last[-1] / last[-2]
            solution[i] = res
            for row in self.converted_matrix:
                row[-2] = row[-1] - row[-2] * res
                row.pop()
                # print(row)
            i -= 1
        self.result = solution
        # print(solution)

    def decorate_result(self) -> str:
        if not self.result:
            self.get_result()
        temp = []
        for i in range(1, self.length+1):
            temp.append(f'X[{str(i)}] = {str(self.result[i])}')
        return '\n'.join(temp)

    def check_result(self, row):
        count = 0
        for i in range(1, self.length + 1):
            count += self.matrix[row][i - 1] * self.result[i]
        return count

    def to_print_check(self):
        res = [[] for _ in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] < 0:
                    if j == 0:
                        res[i].append(f'{str(self.matrix[i][j])}*{str(self.result[j + 1])}')
                        continue
                    res[i].append('-')
                    res[i].append(f'{str(self.matrix[i][j]*-1)}*{str(self.result[j + 1])}')
                else:
                    if j > 0:
                        res[i].append('+')
                    res[i].append(f'{str(self.matrix[i][j])}*{str(self.result[j + 1])}')
            res[i].append('=')
            res[i].append(str(self.check_result(i)))
            res[i].append('expected result: ')
            res[i].append(str(self.matrix[i][-1]))
        temp = [' '.join(x) for x in res]
        res_str = '\n'.join(temp)

        return res_str

