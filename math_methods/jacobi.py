from math_methods.gauss import Gauss


class Jacobi(Gauss):
    def __init__(self, matrix):
        super().__init__(matrix)
        self.matrix = self.convert_matrix(matrix)
        self.x = {i: 0 for i in range(self.matrix[1])}
        self.difference = {i: float('inf') for i in range(self.matrix[1])}
        self.divergence_counter = 0
        self.stop_key = {i: False for i in range(self.matrix[1])}
        self.iterations = 0
        self.success = False

    @staticmethod
    def convert_matrix(matrix):
        for i in range(len(matrix[0])):
            matrix[0][i] = [float(val) for val in matrix[0][i]]
        return matrix

    def update_matrix(self):
        from math_methods.validation import Validation
        if not Validation.jacobi_order:
            self.converted_matrix = self.matrix[0]
            return
        for key in Validation.jacobi_order:
            self.converted_matrix[Validation.jacobi_order[key]] = self.matrix[0][key]

    def jacobi_formula(self):
        new_x = {}
        for i in range(self.matrix[1]):
            new_x[i] = (1 / self.converted_matrix[i][i]) * (self.converted_matrix[i][-1] - self.get_left(i))
        self.check_diff(new_x)
        self.x = new_x

    def get_left(self, row_num):
        res = 0
        for i in range(self.matrix[1]):
            if i == row_num:
                continue
            res += self.converted_matrix[row_num][i] * self.x[i]
        return res

    def check_diff(self, new_x: {}):
        for key in self.x:
            diff = abs(new_x[key] - self.x[key])
            if diff > self.difference[key]:
                self.divergence_counter += 1
            if diff < 1 / 1000000:
                self.stop_key[key] = True
            self.difference[key] = diff

    def get_result(self):
        counter = 0
        while not all(self.stop_key.values()):
            self.jacobi_formula()
            counter += 1
            if self.divergence_counter > 100:
                return
        else:
            self.success = True
            self.result = self.x
        self.iterations = counter
