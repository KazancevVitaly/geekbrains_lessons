# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.


class Worker:
    name = 'Robert'
    surname = 'Summer'
    position = 'bookkeeper'
    _income = {
        'wage': 20000,
        'bonus': 5000
    }

    # Создать класс Position (должность) на базе класса Worker.
    # В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
    # и дохода с учетом премии (get_total_income).
    # Проверить работу примера на реальных данных
    # (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
    # вызвать методы экземпляров).


class Position(Worker):
    def get_full_name(self):
        w1 = f'{Worker.name} {Worker.surname}'
        return w1

    def get_total_income(self):
        inc_w1 = Worker._income.get('wage') + Worker._income.get('bonus')
        return inc_w1


worker1 = Position()
print(f'Доход \033[1m\033[3m{worker1.get_full_name()} \033[0m занимающего должность \033[1m{Worker.position} '
      f'\033[0m составляет \033[1m{worker1.get_total_income():.2f}')


