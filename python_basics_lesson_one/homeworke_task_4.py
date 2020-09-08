# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('самая БОЛЬШАЯ цифра в числе')

number = int(input('Введите любое число:  '))
digit = []
max_digit = 0

while number > 0:
    digit = number % 10
    number = (number - digit) // 10
    if digit > max_digit:
        max_digit = digit

print(f'самая БОЛЬШАЯ цифра в числе {max_digit}')
