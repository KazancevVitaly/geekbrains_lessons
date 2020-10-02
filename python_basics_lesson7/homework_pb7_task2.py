#  Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#  размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__()
        self.size = size
        self.name = name

    def calculation(self):
        a = self.size / 6.5 + 0.5
        return a

    def __str__(self):
        return f'Для пошива {self.name} {self.size} размера нужна ткань в количестве' \
               f' {self.size / 6.5 + 0.5:.2f} метров'


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__()
        self.name = name
        self.height = height

    def calculation(self):
        return 2 * self.height + 0.3

    def __str__(self):
        return f'Чтобы сшить {self.name} на рост {self.height * 100} см. ' \
               f'необходимо {2 * self.height + 0.3:.2f} метров ткани'


coat_fabric = Coat('coat', 48)
print(coat_fabric)
costume_fabric = Costume('costume', 1.7)
print(costume_fabric)
print(f'Всего нужно {coat_fabric.calculation() + costume_fabric.calculation():.2f} метров ткани')

# применить @property
