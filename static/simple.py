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
    for x in range(360):
        bob.pencolor(colors[x % 6])
        bob.width(x / 100 + 1)
        bob.forward(x)
        bob.left(59)


def wormhole(ninja):
    # ninja = turtle.Turtle()
    # ninja.speed(100)
    for i in range(180):
        ninja.forward(200)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)
        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()
        ninja.right(2)