from tkinter import *


class racingCar:

    def __init__(self):
        # Create main window
        window = Tk()
        window.title('Racing Car')

        # Create canvas to draw car in
        self.canvas = Canvas(window, width = 300, height = 200, bg = 'white')
        self.canvas.pack()

        # Starting car coordinates
        self.x = 0
        self.y = 200

        # Key binding to pause, resume, speed-up and speed-down
        window.bind('<Right>', self.rightKey)
        window.bind('<Left>', self.leftKey)
        window.bind('<Up>', self.upKey)
        window.bind('<Down>', self.downKey)

        # Set variables for animation and start animation
        self.animate = True
        self.factor = 1
        self.animateCar()

        window.mainloop()

    # Functions to resume, pause, speed-up and speed-down car
    def rightKey(self, event):
        self.animate = True
        self.animateCar()

    def leftKey(self, event):
        self.animate = False

    def upKey(self, event):
        self.factor += 1

    def downKey(self, event):
        if self.factor > 1:
            self.factor -= 1

    # Function to animate the cars
    def animateCar(self):
        while self.animate:
            if self.x > 300:
                self.x = 0
            else:
                self.x += self.factor
            self.displayCar()
            self.displaySecCar()
            self.canvas.after(100)
            self.canvas.update()

    def displaySecCar(self):
        # Delete car
        self.canvas.delete('car2')

        # Create second car
        self.canvas.create_oval(self.x + 10, self.y - 50, self.x + 20, self.y - 40,
                                fill = 'black', tags = 'car2')
        self.canvas.create_oval(self.x + 30, self.y - 50, self.x + 40, self.y - 40,
                                fill = 'black', tags = 'car2')
        self.canvas.create_rectangle(self.x, self.y - 60, self.x + 50, self.y - 50,
                                    fill = 'red', tags = 'car2')
        self.canvas.create_polygon(self.x + 10, self.y - 60, self.x + 20, self.y - 70,
                                    self.x + 30, self.y - 70, self.x + 40, self.y - 60,
                                    fill = 'black', tags = 'car2')

    def displayCar(self):
        # Delete car
        self.canvas.delete('car')

        # Create first car
        self.canvas.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y,
                                fill = 'black', tags = 'car')
        self.canvas.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y,
                                fill = 'black', tags = 'car')
        self.canvas.create_rectangle(self.x, self.y - 20, self.x + 50, self.y - 10,
                                    fill = 'red', tags = 'car')
        self.canvas.create_polygon(self.x + 10, self.y - 20, self.x + 20, self.y - 30,
                                    self.x + 30, self.y - 30, self.x + 40, self.y - 20,
                                    fill = 'black', tags = 'car')

racingCar()