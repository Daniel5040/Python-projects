from tkinter import *
from random import random


class BeanMachineGUI():
    
    def __init__(self, window):
        # frame for entry options
        top_frame = Frame(window)
        top_frame.pack(side = TOP)

        # entries and buttons for number of slots and balls
        Label(top_frame, text = 'Balls').pack(side = LEFT)
        self.balls = IntVar()
        Entry(top_frame, width = 5, textvariable = self.balls).pack(side = LEFT)
        Label(top_frame, text = 'Slots').pack(side = LEFT)
        self.slots = IntVar()
        Entry(top_frame, width = 5, textvariable = self.slots).pack(side = LEFT)
        Button(top_frame, text = 'Start', command = self.start).pack(side = LEFT)
        Button(top_frame, text = 'Exit', command = window.destroy).pack(side = LEFT)

        # wait till start button is pressed to continue
        self.var = IntVar()
        window.wait_variable(self.var)

    def getVariables(self):
        self.num_balls = self.balls.get() # number of balls
        self.num_slots = self.slots.get() # number of slots
        self.width = self.num_slots * 50 # width of the window
        self.height = 140 + ((self.num_slots -1) * 50) # height of the window
        self.canvas = Canvas(window, width = self.width, height = self.height, bg = 'light blue') # canvas for bean machine
        self.canvas.pack(side = TOP)

    def start(self):
        self.var.set(1)
        self.getVariables()
        self.drawPins()
        self.drawSlots()

    def drawSlots(self):
        slot_size = self.width / self.num_slots # each slot will be 50 px wide

        for i in range(self.num_slots + 1): # Draw the outline of the slots
            if i == 0:
                # draw the first line, otherwise it won't show if start at x = 0
                self.canvas.create_line(3, self.height, 3, self.height - 80, width = 2)
            else:
                # draw the rest of the lines
                self.canvas.create_line(i * slot_size, self.height, i * slot_size, self.height - 80, width = 2)

        # draw the outline of the Bean Machine
        self.canvas.create_line(0, self.height - 80, self.width / 2 - 25, 50, width = 2)
        self.canvas.create_line(self.width, self.height - 80, self.width / 2 + 25, 50, width = 2)
        self.canvas.create_line(self.width / 2 - 25, 50, self.width / 2 - 25, 0, width = 2)
        self.canvas.create_line(self.width / 2 + 25, 50, self.width / 2 + 25, 0, width = 2)

    def drawPins(self):
        pin_x = self.width / self.num_slots
        pin_y = (self.height - 140) / (self.num_slots - 1)

        # draw even number level of pins
        for j in range(int(self.num_slots / 2)):
            for i in range(j + 1, self.num_slots - j):
                self.canvas.create_oval(i * pin_x - 4, self.height - ((j + 1) * pin_x * 2 - 17), i * pin_x + 4,
                self.height - ((j + 1) * pin_y * 2 - 9), fill = 'black')

        # draw odd number level of pins
        for j in range(1, int(self.num_slots / 2) + 1):
            for i in range(j, self.num_slots - j):
                self.canvas.create_oval((i * pin_x - 4) + 25, self.height - (j * pin_y * 2 + 33), (i * pin_x + 4) + 25, 
                self.height - (j * pin_y * 2 + 41), fill = 'black')


class Ball():

    def __init__(self, num, width, height, canvas):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.x = self.width / 2 # starting x coordinate
        self.y = 0 # starting y coordinate
        self.path = [] # starting path variable
        self.num = num # number for tags variable
        self.drawBall()

    def drawBall(self):
        self.canvas.delete('ball' + str(self.num)) # delete ball for new coordinates

        self.canvas.create_oval(self.x - 7, self.y, self.x + 7, self.y + 14, fill = 'red', outline = 'black', tags = 'ball' + str(self.num))

    def fall(self):
        counter = 0 # index for location of pins
        while True:
            if (self.y + 14) < self.height: # keep ball falling until it reaches bottom
                if self.y - 8 == pin_loc[counter] - 8: # if ball reaches a pin
                    self.move_x(counter) # move to either left or right
                    self.drawBall()
                    self.y += 5
                    if counter < len(pin_loc) - 1: # make sure not to go out of bounds for pin_loc
                        counter += 1
                else:
                    self.drawBall()
                    self.y += 5
            else:
                self.y = self.height - 14 # make ball stick to the bottom of the screen
                break # break out of loop so next ball can be animated
            
            self.canvas.after(50)
            self.canvas.update() 

    def move_x(self, counter):
        for i in range(0, 5):
            if self.path[counter] == 'L': # if 'L' move ball to the left
                self.drawBall()
                self.x -= 5
            else: # else move ball to the right
                self.drawBall()
                self.x += 5

            # make the ball "bounce off" the pin
            if i < 2:
                self.y -= 3
            elif i > 2:
                self.y += 3


            self.canvas.after(50)
            self.canvas.update()

def beanMachine(ball):
    path = [] # path taken by the ball
    for j in range (len(slots) - 1): # there are (slots - 1) number of pins the ball will fall through
        leftOrRight(path)
    ball.path = path
    decideSlot(path)

def decideSlot(path):
    slot = 0 # if the ball falls only to the left, the final slot is 
             # the left-most slot
    for i in path: # for every L or R
        if i == 'R':
            slot += 1 # The number of Rs in a path is the position of the 
                      # slot where the ball falls
    slots[slot] += 'O' # add a ball to the final value of slot where the ball would fall

# randomly choose if ball will fall to the left or right side of pin
def leftOrRight(path):
    if random() > 0.5:
        path.append('L')
    else:
        path.append('R')

# draw the histogram
def drawHistogram():
    width = bean.width
    height = 20 * (len(max(slots)) + 1)

    histogram = Canvas(window, width = width, height = height, bg = 'white')
    histogram.pack(side = TOP)

    for i in range(len(slots)):
        histogram.create_rectangle(i * 50, height, (i + 1) * 50, height - (len(slots[i]) * 20), outline = 'black', fill = 'light green')

    frame = Frame(window)
    frame.pack(side = BOTTOM)

    for i in range(1, len(slots) + 1):
        Label(frame, width = 5, text = 'slot ' + str(i)).pack(side = LEFT)


window = Tk() # make a tk object 
window.title('Bean Machine') # set the title for window

bean = BeanMachineGUI(window) # draw the Bean machine

slots = bean.num_slots * [''] # list of slots, '' indicates that no balls are in the slot
pin_loc = [] # list of pin location in y axis
balls = [] # list of balls objects

for i in range(bean.num_balls): # loop to fill the list of balls with ball objects
    balls.append(Ball(i, bean.width, bean.height, bean.canvas))
    beanMachine(balls[i])

for i in range(1, len(balls[0].path) + 1):
    pin_loc.append(40 + (i * 50)) # pin locations

for i in balls: # dropping each of the balls
    i.fall()

drawHistogram()

window.mainloop()