number_list = []
Sum = 0
i = 0
el = None
while el != 'Q':
    user_list = input('Введите строку из чисел, для завершения нажмите Q:  ').split()
    for el in user_list:
        el = el.upper()
        if el == 'Q':
            break
        else:
            try:
                el = float(el)
                number_list.append(el)
            except ValueError:
                print('Error! Вводите числа через пробел, либо символ Q для завершения программы')
    i += 1
    if i <= 1:
        Sum = sum(number_list)
        print(f'{Sum}')
        continue
    a = Sum
    Sum = sum(number_list)
    print(f'({a}), {Sum}')