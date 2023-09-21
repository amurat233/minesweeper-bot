import sys
from guidisplay import GUIDisplay
from gameboard import GameBoard
import pygame

if __name__ == "__main__":
    pygame.init()
    rows, cols, mines, grid_size = (int(i) for i in sys.argv[1:])
    board = GameBoard(rows, cols, mines)
    display = GUIDisplay(board=board, grid_size=grid_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        display.update()

        move = input("Flag (F) or Reveal (R)?")
        row = int(input("Row:"))
        col = int(input("Col:"))

        if move.lower() == "f":
            board.flag(row, col)
        elif move.lower() == "r":
            board.reveal(row, col)
        else:
            running = False
            pygame.quit()
            quit()
        
