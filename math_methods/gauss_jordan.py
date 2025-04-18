from .gauss import Gauss


class GaussJordan(Gauss):
    def __init__(self, matrix):
        super().__init__(matrix)

    def upgrade_diagonal(self):
        for i in range(self.length):
            divisor = self.converted_matrix[i][i]
            for j in range(self.length + 1):
                self.converted_matrix[i][j] = self.converted_matrix[i][j] / divisor

    def __get_reflection(self):
        self.converted_matrix.reverse()
        for row in self.converted_matrix:
            row[:-1] = row[:-1][::-1]

    def upgrade_top(self):
        self.__get_reflection()
        self.update_matrix()
        self.__get_reflection()

    def get_result(self):
        for i in range(self.length):
            self.result[i+1] = self.converted_matrix[i][-1]
