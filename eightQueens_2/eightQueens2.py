from tkinter import *


class MainGUI:

    def __init__(self):
        window = Tk()
        window.title('Eight Queens')

        self.canvas = Canvas(window) # canvas to hold the board
        self.canvas.pack()
        button_frame = Frame(window) # frame to hold the buttons next and exit
        button_frame.pack(side = BOTTOM)

        self.var = IntVar() # variable to change to next solution
        Button(button_frame, text = 'Exit', command = window.destroy).pack(side = LEFT)
        Button(button_frame, text = 'Next solution', command = lambda: self.var.set(1)).pack(side = LEFT)

        self.count = 0 # number of solutions

        # Queen positions
        queens = 8 * [-1] # queens are placed at (i, queens[i])
        # -1 indicates that no queen is placed in the ith row

        queens[0] = 0 # Initially, place a queen at (0, 0) in the 0th row

        # k - 1 indicates the number of queens placed so far
        # We are looking for a position in the kth row to place a queen
        k = 1
        while k >= 0 and self.count <= 53:
            # Find a position to place a queen in the kth row
            j = self.findPosition(k, queens)
            if j < 0:
                queens[k] = -1
                k -= 1 # back track to the previous row
            else:
                queens[k] = j
                if k == 7:
                    self.count += 1
                    self.displayBoard(queens)
                else:
                    k += 1

        window.mainloop()
        

    def findPosition(self, k, queens):
        start = 0 if queens[k] == -1 else (queens[k] + 1)

        for j in range(start, 8):
            if self.isValid(k, j, queens):
                return j # (k, j) is the place to put the queen now

        return -1

    # Return True if a queen can be placed at (k, j)
    def isValid(self, k, j, queens):
        # see if (k, j) is a possible position
        # check the jth column
        for i in range(k):
            if queens[i] == j:
                return False

        # check major diagonal
        row = k - 1
        column = j - 1
        while row >= 0 and column >= 0:
            if queens[row] == column:
                return False
            
            row -= 1
            column -= 1

        # check minor diagonal
        row = k - 1
        column = j + 1
        while row >= 0 and column <= 7:
            if queens[row] == column:
                return False

            row -= 1
            column -= 1

        return True

    def displayBoard(self, queens):
        self.getPictures(queens)
        self.drawBoard()
        self.canvas.update()
        self.canvas.wait_variable(self.var) # wait for next button to be pressed

    def getPictures(self, queens):
        self.pictureRows = [] # store list of images
        for i in range(8):
            self.spots = [] # store images
            self.pictureRows.append(self.spots)
            for j in range(8):
                if j == queens[i]:
                    self.pictureRows[i].append(PhotoImage(file = 'images/queen.gif', width = 75, height = 75))
                else:
                    self.pictureRows[i].append(PhotoImage(file = 'images/red.gif', width = 75, height = 75))

    def drawBoard(self):
        self.nextSolution = False
        self.labelList = [] # store list of labels
        for i in range(8):
            self.labels = [] # list of labels
            self.labelList.append(self.labels)
            for j in range (8):
                self.labelList[i].append(Label(self.canvas, image = self.pictureRows[i][j]))
                self.labelList[i][j].grid(row = i, column = j) # draw the board
        Label(self.canvas, text = 'Solution ' + str(self.count)).grid(row = 8, column = 0, columnspan = 8) # label to show the number of the solution

MainGUI()