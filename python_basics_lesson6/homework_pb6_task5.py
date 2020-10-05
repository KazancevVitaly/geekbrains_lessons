# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”

class Stationery:
    title = 'Draw Maker'

    def draw(self):
        inf = 'Запуск отрисовки'
        return inf


# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.

class Pen(Stationery):
    def draw(self):
        inf = 'запись текста'
        return inf


class Pencil(Stationery):
    def draw(self):
        inf = 'карандашный рисунок'
        return inf


class Handle(Stationery):
    def draw(self):
        inf = 'важные моменты'
        return inf


# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

st = '-' * 100
process = Stationery()
print(f'{process.title} начинает {process.draw()}.')
print(f'\n{st}')
process2 = Pen()
print(f'{process2.title} делает {process2.draw()}.')
print(f'\n{st}')
process3 = Pencil()
print(f'{process3.title} пишет {process3.draw()}.')
print(f'\n{st}')
process4 = Handle()
print(f'{process4.title} отмечает {process4.draw()} в работе.')
