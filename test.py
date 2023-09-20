from gameboard import GameBoard
from textdisplay import TextDisplay

board = GameBoard(10, 10, 15)
display = TextDisplay(board)

while True:
    display.update()
    move = input("Flag (F) or Reveal (R)?")
    row = int(input("Row:"))
    col = int(input("Col:"))

    if move.lower() == "f":
        board.flag(row, col)
    else:
        board.reveal(row, col)