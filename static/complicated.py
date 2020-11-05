import turtle
import random


def flowers(bob):
    turtle.colormode(255)
    bob.speed(0)
    for _ in range(60):
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


#------------------------------------------------------------------------------------------------
def modern_art(bob):
    n = 30  # number of stars
    x = 144  # exterior angle of each star
    angle = 40
    bob.speed(70)
    for i in range(n):
        turtle.colormode(255)
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        bob.pencolor(a, b, c)
        bob.fillcolor(a, b, c)
        bob.begin_fill()
        # loop for drawing each star
        for _ in range(5):
            bob.forward(5 * n - 5 * i)
            bob.right(x)
            bob.forward(5 * n - 5 * i)
            bob.right(72 - x)
        # colour filling complete
        bob.end_fill()
        # rotating for
        # the next star
        bob.rt(angle)


#--------------------------------------------------------------------------------------------------------------------
def polygon(bob):
    bob.speed(0)  # sets the speed of drawing to 0, which is the fastest
    bob.pencolor('white')
    turtle.bgcolor('black')

    x = 0
    bob.up()  # lifts up the pen, so no lines are drawn

    bob.rt(45)
    bob.fd(90)
    bob.rt(135)

    bob.down()
    while x < 120:
        bob.fd(200)
        bob.rt(61)
        bob.fd(200)
        bob.rt(61)
        bob.fd(200)
        bob.rt(61)
        bob.fd(200)
        bob.rt(61)
        bob.fd(200)
        bob.rt(61)
        bob.fd(200)
        bob.rt(61)

        bob.rt(11.1111)
        x = x + 1


#-----------------------------------------------------------------------------------------------------
def color_gamut(bob):
    turtle.setup(width=600, height=500)
    turtle.reset()
    turtle.hideturtle()

    turtle.bgcolor('black')

    c = 0
    x = 0

    colors = [
        #reddish colors
        (1.00, 0.00, 0.00),
        (1.00, 0.03, 0.00),
        (1.00, 0.05, 0.00),
        (1.00, 0.07, 0.00),
        (1.00, 0.10, 0.00),
        (1.00, 0.12, 0.00),
        (1.00, 0.15, 0.00),
        (1.00, 0.17, 0.00),
        (1.00, 0.20, 0.00),
        (1.00, 0.23, 0.00),
        (1.00, 0.25, 0.00),
        (1.00, 0.28, 0.00),
        (1.00, 0.30, 0.00),
        (1.00, 0.33, 0.00),
        (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00),
        (1.00, 0.40, 0.00),
        (1.00, 0.42, 0.00),
        (1.00, 0.45, 0.00),
        (1.00, 0.47, 0.00),
        #orangey colors
        (1.00, 0.50, 0.00),
        (1.00, 0.53, 0.00),
        (1.00, 0.55, 0.00),
        (1.00, 0.57, 0.00),
        (1.00, 0.60, 0.00),
        (1.00, 0.62, 0.00),
        (1.00, 0.65, 0.00),
        (1.00, 0.68, 0.00),
        (1.00, 0.70, 0.00),
        (1.00, 0.72, 0.00),
        (1.00, 0.75, 0.00),
        (1.00, 0.78, 0.00),
        (1.00, 0.80, 0.00),
        (1.00, 0.82, 0.00),
        (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00),
        (1.00, 0.90, 0.00),
        (1.00, 0.93, 0.00),
        (1.00, 0.95, 0.00),
        (1.00, 0.97, 0.00),
        #yellowy colors
        (1.00, 1.00, 0.00),
        (0.95, 1.00, 0.00),
        (0.90, 1.00, 0.00),
        (0.85, 1.00, 0.00),
        (0.80, 1.00, 0.00),
        (0.75, 1.00, 0.00),
        (0.70, 1.00, 0.00),
        (0.65, 1.00, 0.00),
        (0.60, 1.00, 0.00),
        (0.55, 1.00, 0.00),
        (0.50, 1.00, 0.00),
        (0.45, 1.00, 0.00),
        (0.40, 1.00, 0.00),
        (0.35, 1.00, 0.00),
        (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00),
        (0.20, 1.00, 0.00),
        (0.15, 1.00, 0.00),
        (0.10, 1.00, 0.00),
        (0.05, 1.00, 0.00),
        #greenish colors
        (0.00, 1.00, 0.00),
        (0.00, 0.95, 0.05),
        (0.00, 0.90, 0.10),
        (0.00, 0.85, 0.15),
        (0.00, 0.80, 0.20),
        (0.00, 0.75, 0.25),
        (0.00, 0.70, 0.30),
        (0.00, 0.65, 0.35),
        (0.00, 0.60, 0.40),
        (0.00, 0.55, 0.45),
        (0.00, 0.50, 0.50),
        (0.00, 0.45, 0.55),
        (0.00, 0.40, 0.60),
        (0.00, 0.35, 0.65),
        (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75),
        (0.00, 0.20, 0.80),
        (0.00, 0.15, 0.85),
        (0.00, 0.10, 0.90),
        (0.00, 0.05, 0.95),
        #blueish colors
        (0.00, 0.00, 1.00),
        (0.05, 0.00, 1.00),
        (0.10, 0.00, 1.00),
        (0.15, 0.00, 1.00),
        (0.20, 0.00, 1.00),
        (0.25, 0.00, 1.00),
        (0.30, 0.00, 1.00),
        (0.35, 0.00, 1.00),
        (0.40, 0.00, 1.00),
        (0.45, 0.00, 1.00),
        (0.50, 0.00, 1.00),
        (0.55, 0.00, 1.00),
        (0.60, 0.00, 1.00),
        (0.65, 0.00, 1.00),
        (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00),
        (0.80, 0.00, 1.00),
        (0.85, 0.00, 1.00),
        (0.90, 0.00, 1.00),
        (0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        bob.color(color)
        bob.forward(x)
        bob.right(98)
        x = x + 1
        c = c + 0.1
