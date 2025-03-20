import turtle
s = turtle.Screen()
s.bgcolor('black')
square = turtle.Turtle()
square.color('green')
square.shape('circle')
square.pensize(3)
square.fillcolor('orange')


for i in range(0, 4):
    square.forward(150)
    square.left(90)

for i in range(0, 8):
    square.forward(150)
    square.left(45)

for i in range(0, 4):
    square.forward(150)
    square.right(90)

for i in range(0, 8):
    square.forward(150)
    square.right(45)


turtle.done()
