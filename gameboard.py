from random import randint

class GameBoard:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = mines
        self.numflags = 0
        self.__place_mines()
        self.__first_move = True
        self.hidden = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.flags = []

    # places the mines initially
    def __place_mines(self):
        self.mines = [] # stores (row, col) pairs of mine coordinates
        for i in range(self.num_mines):
            row = randint(0, self.rows-1)
            col = randint(0, self.cols-1)
            while (row, col) in self.mines:
                row = randint(0, self.rows-1)
                col = randint(0, self.cols-1)
            self.mines.append((row, col))
        
        self.neighbours = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for row, col in self.mines:
            self.neighbours[row][col] = -1
        for row, col in self.mines:
            for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                if (row + x_off >= 0 and row + x_off < self.rows) and (col + y_off >= 0 and col + y_off < self.cols) and self.neighbours[row+x_off][col+y_off] != -1:
                    self.neighbours[row+x_off][col+y_off] += 1

    # flags a mine
    def flag(self, row, col):
        self.flags.append((row,col))

    # reveals a square, returns true if square was safe and if square empty than it
    # flood reveals all surrounding empty squares until it sees a non-empty square
    def reveal(self, row, col):
        if self.__first_move:
            while (row, col) in self.mines:
                self.__place_mines()
        self.__first_move = False

    # returns a representation of the board that can be analysed but all the hidden
    # squares are not shown.
    def get_board(self):
        ...