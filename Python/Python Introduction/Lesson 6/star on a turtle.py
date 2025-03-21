import turtle

s = turtle.Screen()
s.bgcolor('black')


star = turtle.Turtle()
star.color('green')
star.pensize('3')
star.fillcolor('orange')

star.forward(100)
star.left(120)
star.forward(100)

star.left(120)
star.forward(100)

star.penup()
star.right(150)
star.forward(50)

star.pendown()
star.right(90)
star.forward(100)

star.right(120)
star.forward(100)
star.right(120)
star.forward(100)
#--              ---
star.forward(100)
star.right(120)
star.forward(100)

star.right(120)
star.forward(100)

star.penup()
star.left(150)
star.forward(50)

star.pendown()
star.left(90)
star.forward(100)

star.left(120)
star.forward(100)
star.left(120)
star.forward(100)
#-- --
star.forward(100)
star.left(120)
star.forward(100)

star.left(120)
star.forward(100)

star.penup()
star.right(150)
star.forward(50)

star.pendown()
star.right(90)
star.forward(100)

star.right(120)
star.forward(100)
star.right(120)
star.forward(100)
#---
star.forward(100)
star.right(120)
star.forward(100)

star.right(120)
star.forward(100)

star.penup()
star.left(150)
star.forward(50)

star.pendown()
star.left(90)
star.forward(100)

star.left(120)
star.forward(100)
star.left(120)
star.forward(100)

turtle.done()