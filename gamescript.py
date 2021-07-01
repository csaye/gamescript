import pygame, sys

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# quits game
def quitgame():
    pygame.quit()
    sys.exit()

# game class
class Game:
    clock = pygame.time.Clock()
    events = []
    frame = 0

    def __init__(self, grid=16, width=32, height=32):
        # initialize params
        self.grid = grid
        self.width = width
        self.height = height

        # initialize board
        self.board = [[black for x in range(width)] for y in range(height)]

        # initialize screen
        screen_size = (width * grid, height * grid)
        self.screen = pygame.display.set_mode(screen_size)

    # sets screen caption
    def caption(self, text):
        pygame.display.set_caption(text)

    # draws current board
    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                rect = (x * self.grid, y * self.grid, self.grid, self.grid)
                color = self.board[x][y]
                pygame.draw.rect(self.screen, color, rect)
        pygame.display.update()

    # returns whether game should update
    def isupdate(self):
        return self.frame % 60 == 0

    # ticks update clock
    def tick(self):
        self.frame += 1
        self.draw()
        self.clock.tick(60)
        self.events = pygame.event.get()

    # checks for quit event
    def checkquit(self):
        for event in self.events:
            if event.type == pygame.QUIT: quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: quitgame()
