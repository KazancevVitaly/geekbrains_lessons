# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

winter = ['12', '01', '02']
spring = ['03', '04', '05']
summer = ['06', '07', '08']
autumn = ['09', '10', '11']

month = input('Номер месяца:    ')
month = f'{int(month):02}'

if month in winter:
    print('ЗИМА')
elif month in spring:
    print('ВЕСНА')
elif month in summer:
    print('ЛЕТО')
else:
    print('ОСЕНЬ')
