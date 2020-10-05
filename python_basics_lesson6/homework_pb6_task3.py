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
        w1 = f'{self.name} {self.surname}'
        return w1

    def get_total_income(self):
        inc_w1 = self._income.get('wage') + self._income.get('bonus')
        return inc_w1


worker1 = Position()
print(f'Доход \033[1m\033[3m{worker1.get_full_name()} \033[0m занимающего должность \033[1m{worker1.position} '
      f'\033[0m составляет \033[1m{worker1.get_total_income():.2f}')

worker2 = Position()
worker2.name = 'Kate'
worker2.surname = 'Brown'
worker2.position = 'Secretary'
worker2._income = {
    'wage': 15000,
    'bonus': 5000
}
print(f'Доход \033[1m\033[3m{worker2.get_full_name()} \033[0m занимающего должность \033[1m{worker2.position} '
      f'\033[0m составляет \033[1m{worker2.get_total_income():.2f}')
