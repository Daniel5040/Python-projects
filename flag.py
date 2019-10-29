import turtle

# dimensions for the flag
h = 260
w = 1.9 * h

def main():
    t = turtle.Turtle() # create turtle object
    t.speed(-1) # fastest speed
    # the outline for the flag
    drawFilledRectangle(t, -200, 0, w, h, 'red', 'red')
    # white stripes
    for i in range(20, 250, 40):
        drawFilledRectangle(t, -200, i, w, 20)
    # blue rectangle on top left
    drawFilledRectangle(t, -200, 260, (1 / 3) * w, -(7 / 13) * h, 'blue', 'blue')
    # flag's stars
    for x in range(18, 158, 28):
        for y in range(15, 145, 25):
            drawStar(t, -200 + y, h - x, 10)
    for x in range(32, 144, 28):
        for y in range(30, 155, 25):
            drawStar(t, -200 + y, h - x, 10)

# function to draw a rectangle
def drawFilledRectangle(t, x, y, w, h, colorP = 'white', colorF = 'white'):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + h)
    t.goto(x, y + h)
    t.goto(x, y)
    t.end_fill()

# function to draw a star
def drawStar(t, x, y, s, colorP = 'white', colorF = 'white'):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.left(36)
    t.down()
    for i in range(5):
        t.forward(s)
        t.left(144)
    t.end_fill()
    t.right(36)

main()