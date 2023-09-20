class TextDisplay:
    def __init__(self, board):
        self.board = board

    def update(self):
        board = self.board.get_board()
        for r, row in enumerate(board):
            for c, elem in enumerate(row):
                if elem == -1:
                    board[r][c] = "H"
                elif elem == 9:
                    board[r][c] = "F"
                else:
                    board[r][c] = str(elem)
        for row in board:
            print(" ".join(row))