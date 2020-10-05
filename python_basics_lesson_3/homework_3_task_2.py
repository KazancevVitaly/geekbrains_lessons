# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_name = input('Укажите Ваше имя:  ')
user_lname = input('Укажите Вашу фамилию:  ')
us_yaer_of_b = input('Укажите год Вашего рождения:  ')
user_city = input('Укажите город Вашего проживания:  ')
user_email = input('Ваш e-mail:  ')
user_telef = input('Номер Вашего телефона:  ')


def user_inf(name=user_name, last_name=user_lname, year_of_b=us_yaer_of_b, city_of_r=user_city, email=user_email,
             telef=user_telef):
    return f'имя: {name}, фамилия: {last_name}, год рождения: {year_of_b}, город проживания: {city_of_r}, email: {email}, номер телефона: {telef}'


print(user_inf())
print('-' * 100)


def user_inf_v(**kwargs):
    return kwargs


print(user_inf_v(имя=user_name, фамилия=user_lname, год_рождения=us_yaer_of_b, город_проживания=user_city,
                 email=user_email, телефон=user_telef))
