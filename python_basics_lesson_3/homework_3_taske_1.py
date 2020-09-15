#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_division(dividend, divisor):
    return dividend / divisor


exit = None
while exit != 'нет':
    try:
        user_dvd = int(input('Введите делимое:  '))
        user_dvs = int(input('Введите делитель:  '))
        quotient = func_division(user_dvd, user_dvs)
    except ZeroDivisionError:
        print('Error, делить на ноль нельзя!')
        continue
    except ValueError:
        print('Вы должны ввести числовое значение')
        continue
    print(f'При делении {user_dvd} на {user_dvs} получится {quotient:.2f}')
    exit = input('Желаете продолжить? Да или нет:  ')
    exit = exit.lower()
    if exit != 'да' and exit != 'нет':
        pass
