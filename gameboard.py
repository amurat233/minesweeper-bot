from random import randint

class GameBoard:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = mines
        self.numflags = 0
        self.__place_mines()
        self.__first_move = True
        self.__hidden = [[1 for i in range(self.cols)] for j in range(self.rows)] # 1 if cell is hidden, 0 if not
        self.flags = []
        self.lost = False

    # places the mines initially
    def __place_mines(self):
        self.__mines = [] # stores (row, col) pairs of mine coordinates
        for i in range(self.num_mines):
            row = randint(0, self.rows-1)
            col = randint(0, self.cols-1)
            while (row, col) in self.__mines:
                row = randint(0, self.rows-1)
                col = randint(0, self.cols-1)
            self.__mines.append((row, col))
        
        self.__neighbours = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for row, col in self.__mines:
            self.__neighbours[row][col] = -1
        for row, col in self.__mines:
            for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                if (row + y_off >= 0 and row + y_off < self.rows) and (col + x_off >= 0 and col + x_off < self.cols) and self.__neighbours[row+y_off][col+x_off] != -1:
                    self.__neighbours[row+y_off][col+x_off] += 1

    # flags a mine
    def flag(self, row, col):
        if self.__hidden[row][col]:
            if (row, col) not in self.flags:
                self.flags.append((row,col))
    
    # unflags a mine
    def unflag(self, row, col):
        if self.__hidden[row][col]:
            if (row, col) not in self.flags:
                self.flags.remove((row,col))

    # reveals a square, returns true if square was safe and if square empty than it
    # flood reveals all surrounding empty squares until it sees a non-empty square
    def reveal(self, row, col):
        if self.__first_move:
            while (row, col) in self.__mines or self.__neighbours[row][col] != 0:
                self.__place_mines()
            self.__first_move = False

        # Trivial cases
        if self.__hidden[row][col] == 0:
            return True
        elif (row,col) in self.__mines:
            self.lost = True
            return False
        
        if self.__neighbours[row][col] == 0:
            print("flood filling")
            self.__flood_fill(row, col)
        else:
            self.__hidden[row][col] = 0
    
    def __flood_fill(self, row, col):
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            if self.__hidden[row][col]:
                self.__hidden[row][col] = 0 # unhides current cell
                # attempt to unhide all neighbouring cells recursively
                if self.__neighbours[row][col] == 0:
                    for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                        if (row + y_off >= 0 and row + y_off < self.rows) and (col + x_off >= 0 and col + x_off < self.cols) and self.__neighbours[row+y_off][col+x_off] != -1:
                            queue.append((row+y_off,col+x_off))
        
    # returns a representation of the board that can be analysed but all the hidden
    # squares are not shown.
    def get_board(self):
        board = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.__hidden[row][col]:
                    board[row][col] = -1
                else:
                    board[row][col] = self.__neighbours[row][col]

                if (row, col) in self.flags:
                    board[row][col] = 9
        return board
