import pygame, sys

# quits game
def quitgame():
    pygame.quit()
    sys.exit()

# game class
class Game:
    def __init__(self, grid=16, width=32, height=32):
        # initialize params
        self.grid = grid
        self.width = width
        self.height = height

        # initialize screen
        screen_size = (width * grid, height * grid)
        self.screen = pygame.display.set_mode(screen_size)

    # sets screen caption
    def caption(self, text):
        pygame.display.set_caption(text)
