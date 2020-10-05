# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __add__(self, other):
        return Matrix(self.matrix + other.matrix)

    def __str__(self):
        return f'{self.matrix}'.replace('[', ' ').replace(']', '')


matrix_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(matrix_1)
# print(type(matrix_1))
matrix_2 = Matrix([[3, 2, 1], [3, 2, 1], [3, 2, 1]])
print(f"{'-' * 100}")
print(matrix_2)
print(f"{'-' * 100}")
print(matrix_1 + matrix_2)
matrix_3 = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
print(f"{'-' * 100}")
print(matrix_1 + matrix_2 + matrix_3)

# сделать красивый вывод без скобок ? --- Matrix()