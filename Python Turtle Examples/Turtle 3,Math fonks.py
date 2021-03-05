import turtle
import math

arda = turtle.Turtle()

arda.color("blue")
arda.speed(10)

for x in range(500):
	arda.forward(math.sqrt(x)*10)
	arda.left(170)


turtle.done()