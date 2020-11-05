import turtle


class Simple():
	def __init__(self):
		self.bob=turtle.Turtle()

	#-----------------------------------------------------------------------------------------------------------
	def wormhole(self):

		self.bob.speed(100)
		for i in range(180):
			self.bob.forward(200)
			self.bob.right(30)
			self.bob.forward(20)
			self.bob.left(60)
			self.bob.forward(50)
			self.bob.right(30)
			self.bob.penup()
			self.bob.setposition(0, 0)
			self.bob.pendown()
			self.bob.right(2)
		turtle.done()
#------------------------------------------------------------------------------------------------------------

	def color_spiral(self):
		colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
		self.bob.speed(50)
		for x in range(360):
			self.bob.pencolor(colors[x % 6])
			self.bob.width(x / 100 + 1)
			self.bob.forward(x)
			self.bob.left(59)
		turtle.done()
#-------------------------------------------------------------------------------------------------------------

	def protractor(self):
		for angle in range(0, 360, 15):
			self.bob.setheading(angle)
			self.bob.forward(250)
			self.bob.write(str(angle) + '°')
			self.bob.backward(250)
		turtle.done()
#-------------------------------------------------------------------------------------------------------------

	def something(self):
		pass


#----------------------------------------------------------------------------------------------------------------
'''a= Simple()# for testing purpose only
a.wormhole()'''