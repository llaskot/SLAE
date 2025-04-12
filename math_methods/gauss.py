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
            # print('NEW')
            # for row in self.converted_matrix:
            # print(row)
            for j in range(i):
                # print (self.converted_matrix[i])
                if self.converted_matrix[i][j] == 0:
                    continue
                if self.converted_matrix[i - 1][j] == 0 and i - 1 == j:
                    self.converted_matrix[i], self.converted_matrix[i - 1] = \
                        self.converted_matrix[i - 1], self.converted_matrix[i]
                    continue
                # print('i=', i, 'j=', j)
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
                print(row)
            i -= 1
        self.result = solution
        print(solution)


    def check_result(self):
        for row in self.matrix:
            count = 0
            for i in range(1, self.length+1):
                count += row[i-1] * self.result[i]
            print(count)