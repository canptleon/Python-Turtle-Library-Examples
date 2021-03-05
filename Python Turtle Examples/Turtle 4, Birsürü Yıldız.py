import turtle


arda = turtle.Turtle()
arda.getscreen().bgcolor("#994444")

arda.penup()
arda.goto((-200,100))
arda.pendown()


def star(turtle, boyut):
	if boyut <= 10:
		return
	else:
		turtle.begin_fill()
		for x in range(5):
			turtle.forward(boyut)
			star(turtle, boyut/3)
			turtle.left(216)
		turtle.end_fill()	




star(arda, 316)


turtle.done()



