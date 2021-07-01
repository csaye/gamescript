import gamescript

# set up game class
game = gamescript.Game()
game.caption('example project')

# game loop
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

    # tick update loop
    if game.isupdate():
        pass
