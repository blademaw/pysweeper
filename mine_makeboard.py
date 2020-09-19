# Minesweeper Board Maker

import copy, random, pprint, termtables

def findAdj(a, b, board):
    mineAmt = 0
    a, b = a-1, b-1
    for loc in range(9):
        if not(a < 0 or b < 0):
            try:
                if board[a][b] == 'M':
                    mineAmt+=1
            except IndexError:
                pass
        b += 1
        if (loc+1) % 3 == 0:
            a, b = a + 1, b - 3

    return mineAmt

def initboard(height, length):
    init = [0]
    board = [(copy.deepcopy(init) * length) for i in range(height)]

    return board

def makeboard(height, length, mines, conlist):

    init = [0]
    board = [(copy.deepcopy(init) * length) for i in range(height)]

    conlist = conlist
    minelist = []

    for i in range(mines):
        notConnected = True
        while notConnected:
            rowCoord = random.randint(0,height-1)
            colCoord = random.randint(0,length-1)
            if (rowCoord, colCoord) not in conlist:
                conlist += [(rowCoord, colCoord)]
                minelist += [(rowCoord, colCoord)]
                board[rowCoord][colCoord] = 'M'
                notConnected = False

    for i in range(height):
        for j in range(length):
            if board[i][j] == 'M':
                continue
            board[i][j] = findAdj(i, j, board)

    return board, minelist

def display(board):
    disBoard = copy.deepcopy(board)
    for i in range(len(disBoard)):
        for j in range(len(disBoard[0])):
            if disBoard[i][j] == 0:
                disBoard[i][j] = " "
    t = termtables.to_string(
        disBoard,
        style=termtables.styles.ascii_thin_double
    )
    print(t)

def newdisplay(board, uncovered, flaglist):
    disBoard = copy.deepcopy(board)
    for i in range(len(disBoard)):
        for j in range(len(disBoard[0])):
            if (i, j) in flaglist:
                disBoard[i][j] = "[X]"
            elif (i, j) in uncovered:
                disBoard[i][j] = board[i][j]
                if disBoard[i][j] == 0:
                    disBoard[i][j] = " "
            else:
                disBoard[i][j] = "[]"
    t = termtables.to_string(
        disBoard,
        style=termtables.styles.ascii_thin_double
    )
    print(t)

def locSurround(a, b, board):
    oA, oB = a, b
    a, b = a-1, b-1
    mineAmt = 0
    res, coords = [], []
    for loc in range(9):
        if not(a < 0 or b < 0):
            try:
                res += [board[a][b]]
                coords += [(a, b)]
                if board[a][b] == 'M':
                    mineAmt += 1
            except IndexError:
                pass
        b += 1
        if (loc+1) % 3 == 0:
            a, b = a + 1, b - 3

    return mineAmt, res, coords


# myB = [ [0, 0, 0, 0],
#         [0, 'M', 0, 'M']]

# print(locSurround(0, 0, myB))