import pygame
from gameboard import GameBoard

class GUIDisplay:
    def __init__(self, board: GameBoard, grid_size: int = 40, border_width : int = 3):
        self.grid_size = grid_size
        self.width = board.cols*grid_size
        self.height = board.rows*grid_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg_color = (180, 180, 179)
        self.line_color = (235, 228, 209)
        self.bold_color = (38, 87, 124)
        self.flag_image = pygame.transform.scale(pygame.image.load("./assets/flag.png"), (grid_size, grid_size))
        self.screen.fill(self.bg_color)
        self.rows = board.rows
        self.cols = board.cols
        self.board = board
        self.font = pygame.font.Font('freesansbold.ttf', int(grid_size/2))
        self.draw_grid()

    def draw_grid(self):
        for i in range(self.cols):
            pygame.draw.line(self.screen, self.line_color, (i * self.grid_size,0), (i*self.grid_size, self.height), )
        for i in range(self.rows):
            pygame.draw.line(self.screen, self.line_color, (0, i * self.grid_size), (self.width, i*self.grid_size))

    def fill_grid(self):
        board = self.board.get_board()
        for r, row in enumerate(board):
            for c, elem in enumerate(row):
                X = int(self.grid_size * (c + 0.5))
                Y = int(self.grid_size * (r + 0.5))
                if elem >=0 and elem < 9:
                    if elem == 0:
                        text = self.font.render("0", True, self.line_color)
                    elif elem > 0 and elem < 9:
                        text = self.font.render(str(elem), True, self.bold_color)
                    textRect = text.get_rect()
                    textRect.center = (X,Y)
                    self.screen.blit(text, textRect)
                elif elem == 9:
                    img_rect = self.flag_image.get_rect()
                    img_rect.center = (X,Y)
                    self.screen.blit(self.flag_image, img_rect)


    def update(self):
        self.screen.fill(self.bg_color)
        self.draw_grid()
        self.fill_grid()
        pygame.display.flip()