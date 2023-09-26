import sys
from guidisplay import GUIDisplay
from gameboard import GameBoard
from botcontroller import BotController
import pygame

if __name__ == "__main__":
    pygame.init()
    rows, cols, mines, grid_size = (int(i) for i in sys.argv[1:])
    board = GameBoard(rows, cols, mines)
    display = GUIDisplay(board=board, grid_size=grid_size)
    controller = BotController(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        display.update()

        move = input("Flag (F) or Reveal (R) or Basic (B) or Complex (C)?")

        if move.lower() == "f":
            row = int(input("Row:"))
            col = int(input("Col:"))
            board.flag(row, col)
        elif move.lower() == "r":
            row = int(input("Row:"))
            col = int(input("Col:"))
            board.reveal(row, col)
        elif move.lower() == "b":
            controller.mark_basic_flags()
        elif move.lower() == "c":
            controller.mark_complex_flags()
        else:
            running = False
            pygame.quit()
            quit()
        
