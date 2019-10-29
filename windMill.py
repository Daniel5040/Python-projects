from tkinter import *

width = 200
height = 200
radius = 80


class WindMill:

    def __init__(self):
        window = Tk() # create a window
        window.title('Wind Mill') # title for window

        # Canvas for wind mill
        self.canvas = Canvas(window, bg = 'white', width = width, height = height)
        self.canvas.pack()

        # Buttons used to control the wind mill
        resume_button = Button(window, text = 'Resume', command = self.resume)
        stop_button = Button(window, text = 'Stop', command = self.stop)
        speedup_button = Button(window, text = 'Speed up', command = self.speedUp)
        slowdown_button = Button(window, text = 'Slow down', command = self.slowDown)
        resume_button.pack(side = LEFT)
        stop_button.pack(side = LEFT)
        speedup_button.pack(side = LEFT)
        slowdown_button.pack(side = LEFT)

        # initialize variables for animation
        self.startingAngle = 0 
        self.factor = 5
        self.animate = True

        # start animation
        self.animateFan()

        window.mainloop()
    
    # functions to control the windmill with buttons
    def speedUp(self):
        self.factor += 5

    def slowDown(self):
        if self.factor == 5:
            self.factor = 5
        else:
            self.factor -= 5
    
    def resume(self):
        self.animate = True
        self.animateFan()

    def stop(self):
        self.animate = False

    def animateFan(self):
        while self.animate:
            self.startingAngle += self.factor
            self.displayFan()
            self.canvas.after(100)
            self.canvas.update()

    def displayFan(self):
        self.canvas.delete('fan')
        coordinates = width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius

        self.canvas.create_arc(coordinates, start = self.startingAngle, extent = 30, fill = 'red', tags = 'fan')
        self.canvas.create_arc(coordinates, start = self.startingAngle + 90, extent = 30, fill = 'red', tags = 'fan')
        self.canvas.create_arc(coordinates, start = self.startingAngle + 180, extent = 30, fill = 'red', tags = 'fan')
        self.canvas.create_arc(coordinates, start = self.startingAngle + 270, extent = 30, fill = 'red', tags = 'fan')

WindMill()