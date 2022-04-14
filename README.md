# Conway's Game of Life XP Retreat Exercise



Conway's Game of Life is a 0-player computer game, meaning the evolution of the
game is entirely determined by the game's initial state. For more information on
the game including its rules see
https://en.wikipedia.org/wiki/Conway's_Game_of_Life.

## Instructions

Your task is to implement a Python command line program that provides the core
logic of the game. Some scaffolding is already provided for you to help get
things started.

The entry point for your program is `src/game_of_life.py`. A test file is
at `test/test_game_of_life.py`. Run tests with: `python3 -m unittest`.

Your program will use one of the starter patterns in `patterns/` to initialize
the game board, and then output the states of the game as lines of text to
standard out. For each new state of the game, your program should print a line
of text containing space separated coordinate pairs of the format `x,y`
e.g. `0,0 -4,5 1,1` where each coordinate pair represents a live cell on a
2-dimensional grid.

An executable at `bin/render` is provided that takes lines of text on
standard in and renders a frame of the game to the terminal for each line. The
faster your game can calculate game state, the faster the game will go.

Once you're finished, you will be able to see a visualization of the gameplay by
running:

```
python3 src/game_of_life.py patterns/<pattern_file>.txt | bin/render
```

The smaller you make the text of the terminal, the more of the game you will be
able to see.

