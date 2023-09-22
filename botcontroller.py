from gameboard import GameBoard

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
                            if board[r+y_off][c+x_off] == -1 and (r+y_off,c+x_off) not in self.board.flags:
                                self.board.flag(r+y_off,c+x_off)

                if num_flagged == num_mines:
                     for x_off, y_off in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
                        if (r + y_off >= 0 and r + y_off < self.board.rows) and (c + x_off >= 0 and c + x_off < self.board.cols):
                            if board[r+y_off][c+x_off] == -1:
                                self.board.reveal(r+y_off,c+x_off)
        
        
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