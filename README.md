# Pysweeper

A simple implementation of Minesweeper in Python 3

## Description

Pysweeper is a text-based implementation of Minesweeper using Python 3. The majority of the project was made in one night, and is therefore bound to be fatally inefficient and riddled with bugs, but it works!
Pysweeper isn't at all meant to be a replacement for Microsoft's Minesweeper, as the user has to enter the coordinates of each tile they wish to uncover.

## Controls & Playing the Game

Just incase anyone actually wants to try playing Minesweeper with this.
Run `minegame.py`.

### Rules

* All rules are identical to the classic game.
* The game is lost if the user uncovers a tile with a mine under it
* The game is won if the user uncovers all tiles without mines under them

### Text Representations

* Pysweeper is built with [termtables](https://pypi.org/project/termtables/) for displaying the game grid/board.

* Uncovered tiles are marked with `[]`
* Flaged tiles are marked with `[X]`

### Input

* Users can either uncover tiles or flag them.
	* if a user has already uncovered a tile and attempts to uncover it again, this will result in the game attempting to clear the eight adjacent tiles, clearing them if the number of flagged mines matches that of the selected tile, but will refuse to uncover the tiles if there aren't enough flags.

* Uncovering tiles is done by `>>>u x y`, where `x` and `y` are coordinates on the grid, and `(1, 1)` is the top-left corner.
* Flagging tiles is similarly done with an `f` rather than a `u`.

An example of the first move of a game:
```
Enter board height:     9
Enter board length:     9
Enter amount of mines:  10
```
...
```
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+====+====+====+====+====+====+====+====+====+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
Coordinates "x y" >>>   u 4 4
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | 2  |    |    | 1  | [] | [] |
+----+----+----+----+----+----+----+----+----+
| 1  | 3  | [] | 2  |    |    | 1  | [] | [] |
+----+----+----+----+----+----+----+----+----+
|    | 1  | 1  | 1  |    | 1  | 2  | [] | [] |
+----+----+----+----+----+----+----+----+----+
|    |    |    |    |    | 1  | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
|    |    |    | 1  | 1  | 2  | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
|    |    |    | 1  | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
|    |    |    | 1  | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| 1  | 1  | 2  | 1  | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
| [] | [] | [] | [] | [] | [] | [] | [] | [] |
+----+----+----+----+----+----+----+----+----+
MINES LEFT: 10

>>>
```

## Built with

* [termtables](https://pypi.org/project/termtables/) - For displaying game board

# Changelog

### Version 1.0.0
- Published to github