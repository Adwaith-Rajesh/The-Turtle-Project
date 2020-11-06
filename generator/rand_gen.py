from random import randint, choice


class RandomArt:
    colors_p1 = [
        "#3352BA", "#4E78D7", "#708BD7", "#C7849E", "#C76E95", "#C75B80"
    ]
    colors_p2 = ["#f8f3ea", "#cbe2ef", "#85c1e5", "#5584b1", "#254e7b"]

    grp = [colors_p1, colors_p2]

    def __init__(self, t) -> None:
        t.speed(0)
        self.t = t
        self.pos: tuple = None
        self.fill: bool = False
        self.color: tuple = None
        self.loop: int = 100

    def draw_circle(self):
        self.decide()
        self.t.penup()
        self.t.setpos(*self.pos)
        self.t.pendown()
        self.t.color(*self.color)
        if self.fill:
            self.t.begin_fill()

        self.t.circle(randint(1, 50))

        if self.fill:
            self.t.end_fill()

    def draw_square(self):
        self.decide()
        self.t.color(*self.color)
        self.t.penup()
        self.t.setpos(*self.pos)
        self.t.pendown()

        if self.fill is True:
            self.t.begin_fill()

        a = randint(0, 50)
        for _ in range(4):
            self.t.fd(a)
            self.t.right(90)

        if self.fill is True:
            self.t.end_fill()

    def draw_triangles(self):
        self.decide()
        self.t.color(*self.color)
        self.t.penup()
        self.t.setpos(*self.pos)
        self.t.pendown()

        if self.fill is True:
            self.t.begin_fill()

        angle = 60
        a = randint(0, 50)
        side = choice([self.t.right, self.t.left])

        for _ in range(3):
            self.t.fd(a)
            side(angle * 2)
            self.t.fd(a)

        if self.fill is True:
            self.t.end_fill()

    def start(self):

        for i in range(self.loop):
            func_to_run = [
                self.draw_triangles, self.draw_circle, self.draw_square
            ]
            func = choice(func_to_run)
            func()

    def decide(self):
        yes_no = [True, False]
        x_val = randint(-650, 650)
        y_val = randint(-350, 350)
        self.pos = (x_val, y_val)

        pen_color = choice(choice(self.grp))
        fill_color = choice(choice(self.grp))

        self.fill = choice(yes_no)
        if self.fill:
            self.color = (pen_color, fill_color)

        else:
            self.color = (pen_color, )
