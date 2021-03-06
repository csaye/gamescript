# GameScript

<img height="200px" src="https://user-images.githubusercontent.com/27871609/125567645-7fdb20bb-0d43-40a5-b28b-693a7df32f7d.png">

A wrapper for common Pygame functions.

## Installation

Download [gamescript.py](gamescript.py) and place it inside your project folder.

If necessary, install dependency package Pygame with `pip install pygame`.

All functionality should be immediately accessible through `import gamescript`.

## Documentation

### gamescript

Colors:

```py
gamescript.black
gamescript.white
gamescript.red
gamescript.green
gamescript.blue
```

Methods:

```py
gamescript.quitgame() # quits all processes
```

### Game

Create Game class:

```py
import gamescript
game = gamescript.Game()
```

The Game constructor takes three optional parameters:

```py
class Game(grid=16, height=32, width=32)
```

Methods:

```py
game.caption(text) # sets screen caption

game.draw() # draws current board
game.fill(color) # fills board with given color
game.write(text, color, x, y) # writes given text to the screen
game.display() # updates screen display

game.tick() # runs a tick update on game
game.isupdate() # returns whether game should update
game.checkquit() # checks for any quit event

game.iskeydown(key) # returns whether given key is down
game.ismousedown(button) # returns whether given mouse button is down
game.mousepos() # returns mouse position on grid
```

Updating gameboard:

```py
oldcolor = game.board[x][y]
game.board[x][y] = newcolor
```

Keys:

```
up, right, down, left,
lshift, rshift, lalt, ralt, lcommand, rcommand,
control, tab, enter, escape, delete, capslock
+ any char (e.g. 'q')
```

Buttons:

```
left, middle, right
```

## Example

```py
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
```
