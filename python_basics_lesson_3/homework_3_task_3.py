# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    list_f = [a, b, c]
    return a + b + c - min(list_f)


user_a = int(input('Введите число '))
user_b = int(input('Введите еще одно число '))
user_c = int(input('Введите еще одно число '))
print(f'Сумма наибольших из введенных Вами значений {my_func(user_a, user_b, user_c)}')
