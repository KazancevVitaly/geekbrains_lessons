# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w+', encoding='utf-8') as numbers:
    numbers.write(input('Введите набор чисел через пробел:  \n'))
    numbers.seek(0)
    for el in numbers:
        el = el.split()
        sum_ = 0
        for i in el:
            i = int(i)
            sum_ += i
        print(f'\nСумма данных чисел равна {sum_}', file=numbers)
print(f'Сумма данных чисел равна {sum_}')