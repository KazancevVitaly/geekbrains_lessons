#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_division(dividend, divisor):
    return dividend / divisor


exit_ = None
i = 0
while True:
    while True:
        if i < 1:
            break
        else:
            exit_ = input('Желаете продолжить? Да или нет:  ')
            exit_ = exit_.lower()
            if exit_ != 'да' and exit_ != 'нет':
                print('Error! Вы должны ввести да или нет')
            else:
                break
    if exit_ == 'нет':
        break
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
    i += 1
