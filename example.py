import gamescript

# set up game class
game = gamescript.Game()
game.caption('example project')

# draws frame and text to screen
def draw():
    game.draw() # draw board
    game.write(frame, gamescript.white, 0, 0) # write frame
    game.display() # display changes

# game loop
frame = 0
draw()
while True:
    # tick game loop
    game.tick() # tick game
    game.checkquit() # check for quit

    # input
    if game.iskeydown('c'): # if c presssed
        game.fill(gamescript.black) # clear board
    if game.ismousedown('left'): # if left mouse button pressed
        x, y = game.mousepos() # get mouse position
        game.board[x][y] = gamescript.white # set board to white
        draw() # draw text and board

    # tick update loop
    if game.isupdate():
        frame += 1 # increment frame
        draw() # draw text and board
