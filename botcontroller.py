from gameboard import GameBoard
import itertools

class BotController:
    def __init__(self, board: GameBoard):
        self.board = board

    def mark_basic_flags(self):
        board = self.board.get_board()
        for r, row in enumerate(board):
            for c, elem in enumerate(row):
                if elem == -1 or elem == 9:
                    continue
                
                num_mines = elem
                num_hidden = self.__count_hidden(r,c)
                num_flagged = self.__count_flags(r, c)

                if num_hidden + num_flagged == num_mines:
                    for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                        if (r + y_off >= 0 and r + y_off < self.board.rows) and (c + x_off >= 0 and c + x_off < self.board.cols):
                            if board[r+y_off][c+x_off] == -1:
                                self.board.flag(r+y_off,c+x_off)

                if num_flagged == num_mines:
                     for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                        if (r + y_off >= 0 and r + y_off < self.board.rows) and (c + x_off >= 0 and c + x_off < self.board.cols):
                            if board[r+y_off][c+x_off] == -1:
                                self.board.reveal(r+y_off,c+x_off)

    def mark_complex_flags(self):
        board = self.board.get_board()
        for (r,c),(other_r, other_c) in self.__pairs():
            ufn_a = self.__get_hidden(r, c)
            ufn_b = self.__get_hidden(other_r, other_c)

            mines_a = board[r][c] - self.__count_flags(r,c)
            mines_b = board[other_r][other_c] - self.__count_flags(other_r,other_c)

            if mines_a < mines_b:
                temp = mines_a
                mines_a = mines_b
                mines_b = temp
                temp = ufn_a
                ufn_a = ufn_b
                ufn_b = temp
            
            if mines_a - mines_b == len(ufn_a.difference(ufn_b)):
                for row, col in ufn_a.difference(ufn_b):
                    self.board.flag(row, col)
                for row, col in ufn_b.difference(ufn_a):
                    self.board.reveal(row, col)

                

    # Returns the set of hidden unflagged neighbours of row, col
    def __get_hidden(self, row, col):
        board = self.board.get_board()
        hidden = []
        for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                if (row + y_off >= 0 and row + y_off < self.board.rows) and (col + x_off >= 0 and col + x_off < self.board.cols):
                    if board[row + y_off][col + x_off] == -1:
                        hidden.append((row + y_off, col + x_off))
        return set(hidden)

    # returns (num_hidden, num_flags)
    def __count_hidden(self, row, col):
        board = self.board.get_board()
        num_hidden = 0
        for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                if (row + y_off >= 0 and row + y_off < self.board.rows) and (col + x_off >= 0 and col + x_off < self.board.cols):
                    if board[row + y_off][col + x_off] == -1:
                        num_hidden += 1
        return num_hidden
    
    def __count_flags(self, row, col):
        board = self.board.get_board()
        num_flags = 0
        for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                if (row + y_off >= 0 and row + y_off < self.board.rows) and (col + x_off >= 0 and col + x_off < self.board.cols):
                    if board[row + y_off][col + x_off] == 9:
                        num_flags += 1
        return num_flags
    
    def __pairs(self):
        board = self.board.get_board()
        offsets = list(itertools.chain(*[[(i,j) for j in range(-2,3)] for i in range(-2,3)]))
        offsets.remove((0,0))
        pairs = []

        for r, row in enumerate(board):
            for c, elem in enumerate(row):
                if elem > 0 and elem < 9:
                    for x_off, y_off in offsets:
                        other_r, other_c = r + y_off, c + x_off
                        if other_r >= 0 and other_r < self.board.rows and other_c >= 0 and other_c < self.board.cols:
                            other = board[other_r][other_c]
                            if other > 0 and other < 9 and ((r,c),(other_r, other_c)) not in pairs and ((other_r, other_c), (r,c)) not in pairs:
                                pairs.append(((r,c),(other_r, other_c)))
            
        return pairs
