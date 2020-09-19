# Pysweeper

A simple implementation of Minesweeper in Python 3

## Description

Pysweeper is a text-based implementation of Minesweeper using Python 3. The majority of the project was made in one night, and is therefore bound to be fatally inefficient and riddled with bugs, but it works!
Pysweeper isn't at all meant to be a replacement for Microsoft's Minesweeper, as the user has to enter the coordinates of each tile they wish to uncover.

## Controls & Playing the Game

Just incase anyone actually wants to try playing Minesweeper with this.
Run `mine_game.py`.

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
	* uncovering an already-uncovered tile will result in uncovering the surrounding adjacent 8 tiles, but will refuse to uncover the tiles if there is an incorrect number of flags.

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

* [texttable](https://pypi.org/project/texttable/) - For creating ASCII game board
* [termtables](https://pypi.org/project/termtables/) - For displaying game board

# Changelog

### Version 1.0.0
- Published to github
### Version 1.0.01
- Added user input validation for board initialization & commands
- Removed restart function (to be added)
- Converted globals to arguments