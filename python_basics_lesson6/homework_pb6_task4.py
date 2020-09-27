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
    is_police = False

    def show_speed(self):
        inf = f'Текущая скорость автомобиля {self.name} {choice(self.speed)} km/h'
        return inf

    def go(self):
        move = f'{self.color} \033[0m автомобиль {self.name} едет со скоростью {choice(self.speed)} km/h'
        return move

    def turn(self):
        turn = f'{self.color} \033[0m автомобиль {self.name} повернул на{choice(self.direction)},' \
               f'и движется со скоростью {choice(self.speed)} '
        return turn

    def stop(self):
        info = ['Автомобиль продолжает движение', 'Автомобиль остановился']
        info2 = choice(info)
        return info2


car1 = Car()
a = ()

while True:
    print(car1.go())
    print(car1.turn())
    a = car1.stop()
    print(a)
    if a == 'Автомобиль остановился':
        break
    else:
        print(car1.show_speed())

#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
st = '-' * 100
print(f'\n{st}\n')


class TownCar(Car):

    def show_speed(self):
        s = choice(self.speed)
        if s > 60:
            inf = f'Внимание! Автомобиль {self.name} движется с превышением скорости. ' \
                  f'Скорость автомобиля {s}'
        else:
            inf = f'Текущая скорость автомобиля {self.name} {s} km/h'
        return inf


car2 = TownCar()
car2.name = 'Toyota Aygo'
car2.color = choice(['\033[30m Black', '\033[31m Red', '\033[32m Green',
                     '\033[33m Yellow', '\033[34m Blue'])
a = ()

while True:
    print(car2.go())
    print(car2.turn())
    a = car2.stop()
    print(a)
    if a == 'Автомобиль остановился':
        break
    else:
        print(car2.show_speed())

print(f'\n{st}\n')


class SportCar(Car):
    pass


car_sport = SportCar()
car_sport.name = 'Lotus Exige'
car_sport.speed = range(50, 200)
a = ()

while True:
    print(car_sport.go())
    print(car_sport.turn())
    a = car_sport.stop()
    print(a)
    if a == 'Автомобиль остановился':
        break
    else:
        print(car_sport.show_speed())

print(f'\n{st}\n')


class WorkCar(Car):

    def show_speed(self):
        sp = choice(self.speed)
        if sp > 40:
            inf = f'Внимание! Автомобиль {self.name} движется с превышением скорости. ' \
                  f'Скорость автомобиля {sp}'
        else:
            inf = f'Текущая скорость автомобиля {self.name} {sp} km/h'
        return inf


car_work = WorkCar()
car_work.name = 'ГАЗ-66'
a = ()

while True:
    print(car_work.go())
    print(car_work.turn())
    a = car_work.stop()
    print(a)
    if a == 'Автомобиль остановился':
        break
    else:
        print(car_work.show_speed())

print(f'\n{st}\n')


class PoliceCar(Car):
    pass


police_car = PoliceCar()
police_car.name = 'Полицейский автомобиль LADA Vesta'
police_car.is_police = True
police_car.speed = range(1, 200)
a = ()

while True:
    print(police_car.go())
    print(police_car.turn())
    a = police_car.stop()
    print(a)
    if a == 'Автомобиль остановился':
        break
    else:
        print(police_car.show_speed())

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
