import turtle
import math

t = turtle.Turtle()
t.speed(3)

# Step 1. Move to the starting point (the top of the star) using only relative moves.
t.penup()
t.left(90)      # Face north.
t.forward(100)  # Move upward 100 units to reach the top point.
t.pendown()

# Step 2. Set the heading so that the next line goes from the top to the right point.
# From the top (facing north), a right turn of 135° will point in the direction from top to right.
t.right(135)

# Calculate the side length between the extreme points.
side = 100 * math.sqrt(2)  # Approximately 141.42 units.

# Step 3. Draw the diamond (star outline). Note that each straight line drawn from one extreme to the next
# naturally passes through the midpoint (as in your image).
for _ in range(4):
    t.forward(side)
    t.right(90)  # Turn right 90° at each extreme.

t.hideturtle()
turtle.done()
