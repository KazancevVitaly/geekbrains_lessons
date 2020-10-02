# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data):
        day, month, year = data
        return cls(int(day), int(month), int(year))

    @staticmethod
    def validation_date(self):
        if (self.day >= 1 and self.day <= 31) and (self.month == 1 or self.month == 3 or self.month == 5
                                                   or self.month == 7 or self.month == 8 or self.month == 10
                                                   or self.month == 12):
            return f'{self.day:02}/{self.month:02}/{self.year}'
        elif (self.day >= 1 and self.day <= 28) and self.month == 2 and self.year % 4 != 0:
            return f'{self.day:02}/{self.month:02}/{self.year}'
        elif (self.day >= 1 and self.day <= 29) and self.month == 2 and self.year % 4 == 0:
            return f'{self.day:02}/{self.month:02}/{self.year}'
        elif (self.day >= 1 and self.day <= 30) and (self.month == 4 or self.month == 6 or self.month == 9
                                                     or self.month == 11):
            return f'{self.day:02}/{self.month:02}/{self.year}'
        else:
            return f'Введено недопустимое значение!'


date = f'{input("Введите число: ")}-{input("Введите номер месяца: ")}-{input("Введите год: ")}'
d_1 = Date.get_date(date.replace('-', ' ').split())
print(Date.validation_date(d_1))
