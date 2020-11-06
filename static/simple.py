import turtle


def protractor(bob):
    # bob = turtle.Turtle()
    for angle in range(0, 360, 15):
        bob.setheading(angle)
        bob.forward(250)
        bob.write(str(angle) + '°')
        bob.backward(250)


def color_spiral(bob):
    colors = ["red", 'purple', 'blue', 'green', 'yellow', 'orange']
    # bob = turtle.Turtle()
    # bob.speed(50)
    turtle.bgcolor("black")
    # bob.bgcolor("black")
    for x in range(360):
        bob.pencolor(colors[x % 6])
        bob.width(x / 100 + 1)
        bob.forward(x)
        bob.left(59)


def wormhole(bob):
    # ninja = turtle.Turtle()
    # ninja.speed(100)
    for i in range(180):
        bob.forward(200)
        bob.right(30)
        bob.forward(20)
        bob.left(60)
        bob.forward(50)
        bob.right(30)
        bob.penup()
        bob.setposition(0, 0)
        bob.pendown()
        bob.right(2)


#-----------------------------------------------------------------------------------------------------
def spider_web(bob):
    for i in range(6):
        bob.forward(150)
        bob.backward(150)
        bob.right(60)

    side = 150
    for i in range(15):
        bob.penup()
        bob.goto(0, 0)
        bob.pendown()
        bob.setheading(0)
        bob.forward(side)
        bob.right(120)
        for j in range(6):
            bob.forward(side)
            bob.right(60)
        side = side - 10
