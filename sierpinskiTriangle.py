import turtle

# colors to be used to color the triangles
colors = ['red', 'green', 'blue', 'magenta', 'teal', 'yellow', 'pink']

# function to draw a triangle
def drawTriangle(t, x1, y1, x2, y2, x3, y3, level):
    t.penup()
    t.fillcolor(colors[level]) # color of triangle depends on level
    t.begin_fill()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()

# function to find the midpoint of triangle sides
def findMid(x1, x2):
    return (x1 + x2) / 2

# recursive function to draw triangles
def fractal(t, x1, y1, x2, y2, x3, y3, level):
    # base case
    drawTriangle(t, x1, y1, x2, y2, x3, y3, level)
    if level > 0:
        # Draw bottom left triangles
        fractal(t, x1, y1, findMid(x1, x2), findMid(y1, y2),
                findMid(x1, x3), findMid(y1, y3), level -1)
        # Draw top triangles
        fractal(t, x2, y2, findMid(x3, x2), findMid(y2, y3),
                findMid(x1, x2), findMid(y1, y2), level - 1)
        # Draw bottom right triangles
        fractal(t, x3, y3, findMid(x1, x3), findMid(y1, y3),
                findMid(x3, x2), findMid(y3, y2), level -1)

def main():
    t = turtle.Turtle() # create turtle object
    t.speed(-1) # fastest speed
    size = 200
    fractal(t, -size, -size, size, -size, 0, size, 5)
    t.hideturtle()

main()