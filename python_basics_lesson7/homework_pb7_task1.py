# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, vector1, vector2, vector3):
        self.vector1 = vector1
        self.vector2 = vector2
        self.vector3 = vector3
        self.matrix = [self.vector1, self.vector2, self.vector3]

    def __add__(self, other):
        return Matrix(
            [int(n) + int(m) for n, m in zip(self.vector1.split(' '), other.vector1.split(' '))],
            [int(n) + int(m) for n, m in zip(self.vector2.split(' '), other.vector2.split(' '))],
            [int(n) + int(m) for n, m in zip(self.vector3.split(' '), other.vector3.split(' '))]
        )
        # self.vector1 = ' '.join(map(str, [int(n) + int(m) for n, m in zip(self.vector1.split(' '),
        #                                                                   other.vector1.split(' '))]))
        # self.vector2 = ' '.join(map(str, [int(n) + int(m) for n, m in zip(self.vector2.split(' '),
        #                                                                   other.vector2.split(' '))]))
        # self.vector3 = ' '.join(map(str, [int(n) + int(m) for n, m in zip(self.vector3.split(' '),
        #                                                                   other.vector3.split(' '))]))
        # self.matrix = [self.vector1, self.vector2, self.vector3]
        # return f'{self.vector1}\n{self.vector2}\n{self.vector3}'

    def __str__(self):
        self.vector1 = ' '.join(map(str, self.vector1))
        self.vector2 = ' '.join(map(str, self.vector2))
        self.vector3 = ' '.join(map(str, self.vector3))
        return f'{self.vector1}\n{self.vector2}\n{self.vector3}'


m_1 = Matrix([10, 20, 30], [10, 20, 30], [10, 20, 30])
print(m_1)
print(f'-' * 100)
m_2 = Matrix([30, 20, 10], [30, 20, 10], [30, 20, 10])
print(m_2)
print(f'-' * 100)
print(m_1 + m_2)
# m_3 = Matrix([40, 40, 40], [40, 40, 40], [40, 40, 40])
# print(m_1 + m_2 + m_3)  ---- ?
