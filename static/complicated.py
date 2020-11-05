import turtle
import random


class Complicated():
	def __init__(self):
		self.bob=turtle.Turtle()
		
	def flowers(self):
		turtle.colormode(255)
		self.bob.speed(100)
		for n in range(60):
			self.bob.penup()
			self.bob.goto(random.randint(-700, 700), random.randint(-700, 700))
			self.bob.pendown()
			red_amount = random.randint(1, 255)  #/ 100.0
			blue_amount = random.randint(1, 255)  #/ 100.0
			green_amount = random.randint(1, 255)  # / 100.0
			self.bob.pencolor((red_amount, green_amount, blue_amount))
			circle_size = random.randint(10, 40)
			self.bob.pensize(random.randint(1, 5))
			for i in range(6):
				self.bob.circle(circle_size)
				self.bob.left(60)
		turtle.done()


#--------------------------------------------------------------------------------------------------------------------
'''a= Complicated()
a.flowers()'''