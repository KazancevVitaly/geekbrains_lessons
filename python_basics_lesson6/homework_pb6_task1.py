#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный.
#  В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#  Продолжительность первого состояния (красный) составляет 7 секунд,
#  второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#  Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    color = ()

    def running(self):
        while True:
            TrafficLight.color = 'RED'
            print(f'\033[31m{TrafficLight.color}')
            sleep(7)
            TrafficLight.color = 'YELLOW'
            print(f'\033[33m{TrafficLight.color}')
            sleep(2)
            TrafficLight.color = 'GREEN'
            print(f'\033[32m{TrafficLight.color}')
            sleep(7)


trafficlight_1 = TrafficLight()
trafficlight_1.running()
