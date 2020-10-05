#  Реализовать проект «Операции с комплексными числами».
#  Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
#  Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров.
#  Проверьте корректность полученного результата.

print('"Операции с комплексными числами"')


class ComplexNumber:
    def __init__(self, complex_number):
        self.complex_number = complex(complex_number)

    def __add__(self, other):
        return ComplexNumber(self.complex_number + other.complex_number)

    def __mul__(self, other):
        return ComplexNumber(self.complex_number * other.complex_number)

    def __str__(self):
        return f'{self.complex_number}'


c_number1 = ComplexNumber(2 + 3j)
c_number2 = ComplexNumber(5 + 7j)

print(c_number1 + c_number2)

print(c_number1 * c_number2)
