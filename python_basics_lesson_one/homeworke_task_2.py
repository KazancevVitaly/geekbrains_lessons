# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print(' "Калькулятор времени" ')

number = int(input('Введите количество секунд:  '))

hour = number // 3600
if hour < 10:
    hour = str(f'0{hour}')

minutes = number % 3600 // 60
if minutes < 10:
    minutes = str(f'0{minutes}')

seconds = number % 3600 % 60
if seconds < 10:
    seconds = str(f'0{seconds}')

print(f'{hour} : {minutes} : {seconds}')
