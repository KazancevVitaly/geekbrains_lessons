# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce


def my_func(a, b):
    return a * b


start = 100
stop = 1000
step = 1
stop = stop + step

my_list = [el for el in range(start, stop, step) if el % 2 == 0]
print(my_list)
mega_number = reduce(my_func, my_list)
print(mega_number)
