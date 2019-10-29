import turtle

# simple function to draw a line
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def fractal(t, x1, y1, x2, y2, level):
    # base case
    if level == 0:
        drawLine(t, x1, y1, x2, y2)
    else:
        newX = (x1 + x2) / 2 + (y2 - y1) / 2
        newY = (y1 + y2) / 2 - (x2 - x1) / 2
        fractal(t, x1, y1, newX, newY, level - 1)
        fractal(t, newX, newY, x2, y2, level - 1)

def main():
    t = turtle.Turtle() # make turtle object
    t.speed(-1) # fastest speed
    t.pencolor('green')
    size = 100
    fractal(t, -size, 0, size, 0, 7)
    t.hideturtle()

main()