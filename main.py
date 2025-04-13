from math_methods.gauss import Gauss
from functions.process_file import get_matrix
from fractions import Fraction

if __name__ == '__main__':

    gs = Gauss(get_matrix('slae6'))
    for row in gs.matrix:
        print(row)

    gs.update_matrix()
    print('RESULT')
    for row in gs.converted_matrix:
        print(row)

    print('RESULT')

    gs.get_result()

    gs.check_result()

    pass
