import gamescript

# set up game class
game = gamescript.Game()
game.caption('example project')

# game loop
while True:
    game.tick() # tick game
    game.checkquit() # check for quit
    if game.isupdate(): print('update') # update loop
