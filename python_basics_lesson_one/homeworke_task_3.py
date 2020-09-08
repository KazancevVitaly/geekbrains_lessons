# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

print('Funny Calculator')

n = int(input('Введите любое число:  '))

nn = int(f'{n}{n}')

nnn = int(f'{n}{n}{n}')

result = n + nn + nnn
print(result)
