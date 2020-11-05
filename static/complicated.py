import turtle
import random


class Complicated():
    def flowers(self):
        bob = turtle.Turtle()
        turtle.colormode(255)
        bob.speed(100)
        for n in range(60):
            bob.penup()
            bob.goto(random.randint(-700, 700), random.randint(-700, 700))
            bob.pendown()
            red_amount = random.randint(1, 255)  #/ 100.0
            blue_amount = random.randint(1, 255)  #/ 100.0
            green_amount = random.randint(1, 255)  # / 100.0
            bob.pencolor((red_amount, green_amount, blue_amount))
            circle_size = random.randint(10, 40)
            bob.pensize(random.randint(1, 5))
            for i in range(6):
                bob.circle(circle_size)
                bob.left(60)
        turtle.done()


#--------------------------------------------------------------------------------------------------------------------
'''a= Complicated()
a.flowers()'''