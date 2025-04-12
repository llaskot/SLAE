from fractions import Fraction
from typing import Union, List, Any


def process_line(line: str) -> list[Fraction]:
    str_row = line.split()
    try:
        matr_row = [Fraction(val) for val in str_row]
    except ValueError as e:
        print(e)
        return []
    return matr_row


def get_matrix(file_path = '../slae'):
    length = 0
    matrix = []
    with open(file_path, 'r') as file:
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
    return matrix, length


if __name__ == "__main__":
    print(get_matrix('../slae'))
