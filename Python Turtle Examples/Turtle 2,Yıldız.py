import turtle

arda = turtle.Turtle()

arda.color("red","yellow")

arda.speed(8)
arda.begin_fill()
for x in range(50):
	arda.forward(300)
	arda.left(170)


arda.end_fill()
		
turtle.done()