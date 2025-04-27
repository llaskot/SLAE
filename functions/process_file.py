from fractions import Fraction


def process_line(line: str) -> list[Fraction]:
    str_row = line.split()
    matr_row = [Fraction(val) for val in str_row]
    return matr_row


def get_matrix(file_path='../slae'):
    length = 0
    matrix = []
    with open(file_path, 'r') as file:
        try:
            for line in file:
                if not line.strip():
                    continue
                if not length:
                    length = int(line)
                    continue
                temp = process_line(line)
                if not temp:
                    return
                matrix.append(temp)
        except ValueError as e:
            length = 0
            matrix = []
    return matrix, length


def to_print(matrix: ()) -> ():
    str_matrix = [[str(elem) for elem in row] for row in matrix[0]]
    max_lengths = []
    for col in zip(*str_matrix):
        max_len = max(len(elem) for elem in col)
        max_lengths.append(max_len)

    matr = '\nMATRIX:\n' + str(matrix[1]) + '\n' + '\n'.join(
        '  '.join(elem.rjust(length) for elem, length in zip(row, max_lengths))
        for row in str_matrix)
    slae = [[] for _ in range(len(matrix[0]))]
    for j in range(len(matrix[0])):
        for i in range(matrix[1]):
            if matrix[0][j][i] < 0:
                if len(slae[j]) == 0:
                    slae[j].append(f'{str_matrix[j][i]}X[{i + 1}]')
                    continue
                slae[j].append('-')
                if matrix[0][j][i] == -1:
                    slae[j].append(f'X[{i + 1}]')
                else:
                    slae[j].append(f'{str_matrix[j][i][1:]}X[{i + 1}]')
            elif matrix[0][j][i] == 0:
                continue
            else:
                if len(slae[j]) > 0:
                    slae[j].append('+')
                if matrix[0][j][i] == 1:
                    slae[j].append(f'X[{i + 1}]')
                else:
                    slae[j].append(f'{str_matrix[j][i]}X[{i + 1}]')

        slae[j].append('=')
        slae[j].append(str_matrix[j][-1])
    temp = [' '.join(x) for x in slae]
    slae_str = '\nSLAE: \n' + '\n'.join(temp)
    return matr, slae_str


if __name__ == "__main__":
    print(get_matrix('../slae'))
