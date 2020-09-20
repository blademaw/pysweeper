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
    """Displays the intiial gameboard given as argument via termtables"""
    # create copy of board, 
    disBoard = copy.deepcopy(board)
    for i in range(len(disBoard)):
        for j in range(len(disBoard[0])):
            if disBoard[i][j] == 0:
                disBoard[i][j] = " "
    
    # adding row and column numbers
    disBoard = [[i for i in range(1, len(disBoard[0])+1)]] + disBoard + [[i for i in range(1, len(disBoard[0])+1)]]
    t = termtables.to_string(
        disBoard,
        style=termtables.styles.ascii_thin_double
    )
    t = t.split("\n")
    del t[0]

    # accounting for digits >8 (to tab board further)
    j = 1
    tabspace = int((len(str(len(disBoard))) % 8 - len(str(len(disBoard)))) / 8) + 1
    print("\n\t"*tabspace + t[0].replace("|", " "))
    print()
    print("\t"*tabspace + t[1])
    for i in range(2, len(t)-3):
        if i % 2 == 0:
            t[i] = str(j) + "\t"*tabspace + t[i] + " "*8 + str(j)
            j += 1
        else:
            t[i] = "\t"*tabspace + t[i]
        print(t[i])
    print("\t"*tabspace + t[-3])
    print("\n\t"*tabspace + t[-2].replace("|", " "))
    print()

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
    disBoard = [[i for i in range(1, len(disBoard[0])+1)]] + disBoard + [[i for i in range(1, len(disBoard[0])+1)]]
    t = termtables.to_string(
        disBoard,
        style=termtables.styles.ascii_thin_double
    )
    t = t.split("\n")
    del t[0]
    j = 1
    tabspace = int((len(str(len(disBoard))) % 8 - len(str(len(disBoard)))) / 8) + 1
    print("\n\t"*tabspace + t[0].replace("|", " "))
    print()
    print("\t"*tabspace + t[1])
    for i in range(2, len(t)-3):
        if i % 2 == 0:
            t[i] = str(j) + "\t"*tabspace + t[i] + " "*8 + str(j)
            j += 1
        else:
            t[i] = "\t"*tabspace + t[i]
        print(t[i])
    print("\t"*tabspace + t[-3])
    print("\n\t"*tabspace + t[-2].replace("|", " "))
    print()

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

# x = [[i for i in range(1,10)]]
# t = termtables.to_string(x, style=termtables.styles.markdown)
# print(t)