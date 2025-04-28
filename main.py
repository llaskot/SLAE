from math_methods.gauss import Gauss
from functions.process_file import get_matrix, to_print
from fractions import Fraction

from math_methods.jacobi import Jacobi
from math_methods.validation import Validation
from math_methods.cramer import Cramer
from math_methods.gauss_jordan import GaussJordan

if __name__ == '__main__':
    mat = get_matrix('jacoby1')
    print(mat)
    print(to_print(mat)[0])
    valid = Validation(mat)
    print(valid._validate_jacobi())
    print(valid.jacobi_order)
    jac = Jacobi(mat)
    jac.update_matrix()
    print(jac.converted_matrix)
    # print(to_print((jac.converted_matrix, mat[1]))[0])
    print(jac.difference)
    print(jac.stop_key)


    jac.get_result()

    print(jac.x)
    print(jac.divergence_counter)
    print(jac.iterations)
    print(jac.success)



    # print(jac.converted_matrix)
    # print(jac.x)
    # gj = GaussJordan(mat)
    # gj.update_matrix()
    # gj.upgrade_diagonal()
    # print(to_print((gj.converted_matrix, len(gj.converted_matrix)))[0])
    # gj.upgrade_top()
    # print(to_print((gj.converted_matrix, len(gj.converted_matrix)))[0])
    # gj.get_result()
    # print(gj.decorate_result())
    # print(gj.to_print_check())

    # c = Cramer(mat)
    # c.get_result()
    # print(c.decorate_result())
    # print(c.to_print_check())

    # print(mat)
    # va = Validation(mat)
    # va.get_square_matrix()
    # print(va.get_determinant())

    # gs = Gauss(get_matrix('slae5'))

    # for row in gs.matrix:
    #     print(row)

    # print(to_print(get_matrix('slae5'))[0])
    # print(to_print(get_matrix('slae5'))[1])

    # gs.update_matrix()
    # print('RESULT')
    # # for row in gs.converted_matrix:
    # #     print(row)
    # upd_matrix = gs.converted_matrix
    # tp = to_print((upd_matrix, len(upd_matrix)))
    # print(tp[0])
    # print(tp[1])

    # print('RESULT')
    #
    # print(gs.decorate_result())
    #
    # gs.check_result()

    pass
