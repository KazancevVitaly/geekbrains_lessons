class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number < other.number:
            return 'impossible'
        else:
            return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __floordiv__(self, other):
        if self.number < other.number:
            return 'impossible'
        else:
            return self.number // other.number

    def __str__(self):
        return f'{self.number}'

    def make_oder(self, rows):
        s = '\u2623' * rows + '\n'
        a = self.number // rows
        remains = self.number % rows
        t = '\u2623' * remains
        print(s * a, end='')
        print(t)


cell_1 = Cell(17)
print(cell_1)
cell_2 = Cell(3)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
cell_1.make_oder(4)


