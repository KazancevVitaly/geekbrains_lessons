#  Реализуйте базовый класс Car.
#  У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула (куда).

from random import choice


class Car:
    speed = range(1, 100)
    color = choice(['\033[30m Black', '\033[31m Red', '\033[32m Green',
                    '\033[33m Yellow', '\033[34m Blue'])
    name = 'LADA'
    direction = ['право', 'лево']
    is_polis = False

    def show_speed(self):
        inf = f'Текущая скорость автомобиля {Car.name} {choice(Car.speed)}'
        return inf

    def go(self):
        move = f'{Car.color} \033[0m автомобиль {Car.name} едет со скоростью {choice(Car.speed)} km/h'
        return move

    def turn(self):
        turn = f'{Car.color} \033[0m автомобиль {Car.name} повернул на{choice(Car.direction)},' \
               f'и движется со скоростью {choice(Car.speed)} '
        return turn

    def stop(self):
        info = ['Автомобиль продолжает движение', 'Автомобиль остановился']
        info2 = choice(info)
        return info2


car1 = Car()

while True:
    print(car1.go())
    print(car1.turn())
    print(car1.stop())
    if car1.stop( ):
        break


#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
