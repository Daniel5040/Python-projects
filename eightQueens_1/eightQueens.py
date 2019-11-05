from tkinter import *


class MainGUI:

    def __init__(self):
        window = Tk()
        window.title('Eight Queens')

        self.main_frame = Frame(window) # frame to hold the board
        self.main_frame.pack()

        # Queen positions
        queens = 8 * [-1] # queens are placed at (i, queens[i])
        # -1 indicates that no queen is currently placed in the ith row
        
        queens[0] = 0 # Initially, place a queen at (0, 0) in the 0th row

        # k - 1 indicates the number of queens placed so far
        # We are looking for a position in the kth row to place a queen
        k = 1
        while k >= 0 and k <= 7:
            # Find a position to place a queen in the kth row
            j = self.findPosition(k, queens)
            if j < 0:
                queens[k] = -1
                k -= 1 # back track to the previous row
            else:
                queens[k] = j
                k += 1

        self.getPictures(queens)
        self.drawBoard()

        window.mainloop()

    def findPosition(self, k, queens):
        start = 0 if queens[k] == -1 else (queens[k] + 1)

        for j in range(start, 8):
            if self.isValid(k, j, queens):
                return j # (k, j) is the place to put the queen no
        
        return -1
        
    # Return True if a queen can be placed at (k, j)
    def isValid(self, k, j, queens):
        # See if (k, j) is a possible position
        # Check the jth column
        for i in range(k):
            if queens[i] == j:
                return False

        # Check major diagonal
        row = k - 1
        column = j - 1
        while row >= 0 and column >= 0:
            if queens[row] == column:
                return False

            row -= 1
            column -= 1

        # Check minor diagonal
        row = k - 1
        column = j + 1
        while row >= 0 and column <= 7:
            if queens[row] == column:
                return False
            
            row -= 1
            column -= 1
        
        return True

    def getPictures(self, queens):
        self.pictureRows = [] # store list of rows
        for i in range (8):
            self.spots = [] # store list of images
            self.pictureRows.append(self.spots)
            for j in range(8):
                if j == queens[i]: 
                    self.pictureRows[i].append(PhotoImage(file = 'images/queen.gif', width = 75, height = 75))
                else:
                    self.pictureRows[i].append(PhotoImage(file = 'images/red.gif', width = 75, height = 75))

    def drawBoard(self):
        self.labelList = [] # store list of labels
        for i in range(8):
            self.labels = [] # list of labels
            self.labelList.append(self.labels)
            for j in range(8):
                self.labelList[i].append(Label(self.main_frame, image = self.pictureRows[i][j]))
                self.labelList[i][j].grid(row = i, column = j) # draw the board


MainGUI()