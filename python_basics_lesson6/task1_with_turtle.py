import turtle
from time import sleep


class TrafficLight:
    __color = ()

    def step1(self):
        t = turtle.Turtle()
        turtle.screensize(800, 800, )
        t.penup()
        t.setpos(-100, -300)
        t.pendown()
        for i in range(2):
            t.fd(200)
            t.left(90)
            t.fd(600)
            t.left(90)
            i += 1
        t.setpos(0, -300)
        t.circle(100)
        t.penup()
        t.setpos(0, -100)
        t.pendown()
        t.circle(100)
        t.penup()
        t.setpos(0, 100)
        t.pendown()
        t.circle(100)
        return

    def step2(self):
        while True:
            t = turtle.Turtle()
            t.penup()
            t.setpos(0, 100)
            t.pendown()
            t.color('red', 'red')
            t.begin_fill()
            t.circle(100)
            t.end_fill()
            sleep(7)
            t.color('yellow', 'yellow')
            t.begin_fill()
            t.circle(-100)
            t.end_fill()
            sleep(2)
            t.color('black', 'white')
            t.begin_fill()
            t.circle(100)
            t.end_fill()

            a = turtle.Turtle()
            a.penup()
            a.setpos(0, 100)
            a.pendown()
            a.color('black', 'white')
            a.begin_fill()
            a.circle(-100)
            a.end_fill()

            t.penup()
            t.setpos(0, -100)
            t.pendown()
            t.color('green', 'green')
            t.begin_fill()
            t.circle(-100)
            t.end_fill()
            sleep(7)
            t.color('black', 'white')
            t.begin_fill()
            t.circle(-100)
            t.end_fill()
            a.color('yellow', 'yellow')
            a.begin_fill()
            a.circle(-100)
            a.end_fill()
            sleep(2)
            a.color('black', 'white')
            a.begin_fill()
            a.circle(-100)
            a.end_fill()


traffic_light = TrafficLight()
traffic_light.step1()
traffic_light.step2()
# t.color("black", "red")
# t.begin_fill()
# t.circle(80)
# t.end_fill()
