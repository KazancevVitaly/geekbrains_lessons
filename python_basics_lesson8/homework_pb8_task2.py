#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#  Проверьте его работу на данных, вводимых пользователем.
#  При вводе пользователем нуля в качестве делителя
#  программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Какое число будем делить?\n')
b = input('На что будем делить Ваше число?\n')

try:
    if b == '0':
        raise OwnError(f'Вы пытаетесь поделить {a} на 0? делить на 0 нельзя!')
    else:
        division = int(a) / int(b)
except (ZeroDivisionError, OwnError) as error:
    print(error)
except ValueError:
    print('Ошибка! Вы ввели нечисловое значение!')
else:
    print(f'{a} / {b} = {division:.2f}')
