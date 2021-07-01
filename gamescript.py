import pygame, sys

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

keyords = {
    'up': 1073741906,
    'right': 1073741903,
    'down': 1073741905,
    'left': 1073741904,
    'lshift': 1073742049, 'rshift': 1073742053,
    'lalt': 1073742050, 'ralt': 1073742054,
    'lcommand': 1073742051, 'rcommand': 1073742055,
    'control': 1073742048,
    'tab': 9,
    'enter': 13,
    'escape': 27,
    'delete': 8,
    'capslock': 1073741881
}

buttonords = {
    'left': 1,
    'middle': 2,
    'right': 3
}

# returns ord of given key
def keyord(key):
    if len(key) == 1: return ord(key)
    if key in keyords: return keyords[key]
    raise ValueError(f'invalid key: \'{key}\'')

# returns ord of given button
def buttonord(button):
    if button in buttonords: return buttonords[button]
    raise ValueError(f'invalid button: \'{button}\'')

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

    # fills board with given color
    def fill(self, color):
        self.board = [[color for x in range(self.width)] for y in range(self.height)]

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

    # checks whether given key is down
    def iskeydown(self, key):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == keyord(key): return True
        return False

    # returns whether given mouse button is down
    def ismousedown(self, button):
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == buttonord(button): return True
        return False

    # returns mouse position on grid
    def mousepos(self):
        mousex, mousey = pygame.mouse.get_pos()
        x = mousex // self.grid
        y = mousey // self.grid
        return x, y
