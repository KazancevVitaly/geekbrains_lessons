#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name_script, wph, sph, bon = argv


def func_salary(w_per_hour, salary_per_hour, bonus):
    return w_per_hour * salary_per_hour + bonus


print(f'{func_salary(float(wph), float(sph), float(bon)):.2f}')
