import mine_makeboard, minetest, copy

uncovered, flaglist, finalBoard = [], [], []
height, length, mines = 0, 0, 0
gameRunning = True

def getInput():
    boardHeight = int(input("Enter board height:\t"))
    boardLength = int(input("Enter board length:\t"))
    mineInput = int(input("Enter amount of mines:\t"))

    return boardHeight, boardLength, mineInput

def hideboard(board):
    hidden = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            hidden[i][j] = "[]"
    
    return hidden

def startMove(height, length, mines, board):
    global uncovered
    move = [(int(i)-1) for i in ((input("Coordinates \"x y\" >>>\t")).split(" "))[1:]]
    b, a = move
    surList = mine_makeboard.locSurround(a, b, board)[2]

    finBoard, minelist = mine_makeboard.makeboard(height, length, mines, surList)
    uncovered += minetest.auxG(finBoard, (a, b))
    return finBoard, minelist

def uncover(board, pos):
    global uncovered, flaglist
    a, b = pos
    if pos in uncovered:
        minecount = 0
        mineAmt, _, coords = mine_makeboard.locSurround(a, b, board)
        for coord in coords:
            if coord in flaglist:
                minecount += 1
        if minecount == mineAmt:
            for coord in coords:
                if coord not in uncovered and coord not in flaglist:
                    cA, cB = coord[0], coord[1]
                    for ret in minetest.auxG(board, (cA, cB)):
                        if ret not in uncovered:
                            uncovered += [ret]
        else:
            print("\nNon-matching mine count.\n")
    else:
        if pos in uncovered:
            print("\nCannot uncover an already uncovered square.\n")
        elif pos in flaglist:
            print("\nCannot uncover a flagged square.\n")
        else:
            for ret in minetest.auxG(board, (a, b)):
                if ret not in uncovered:
                    uncovered += [ret]

def flag(board, pos):
    global flaglist, uncovered
    if pos in uncovered:
        print("\nYou cannot flag an uncovered square.\n")
    elif pos in flaglist:
        flaglist.remove(pos)
    else:
        flaglist += [pos]

def checkLoss():
    global uncovered, minelist
    for potential in uncovered:
        if potential in minelist:
            gameOver()

def gameOver():
    global gameRunning
    gameRunning = False
    print("\n\n\nYOU LOSE!\n\n\n")

def winning():
    global gameRunning, flaglist, uncovered, minelist
    flaglist = minelist
    mine_makeboard.newdisplay(finalBoard, uncovered, flaglist)
    print("\n\n\nYOU WIN!!!!!!!!\n\n\n")
    startAgain = input("Restart? [y/n]: ")
    if startAgain == 'y':
        gameRunning = True
        startGame()
    else:
        gameRunning = False

def startGame():
    global height, length, mines, finalBoard, minelist
    height, length, mines = getInput()
    initBoard = mine_makeboard.initboard(height, length)
    startBoard = hideboard(initBoard)
    print("\nWelcome to minesweeper!\nTo uncover a tile, enter in the format: 'u x y' with spaces.")
    print("To flag, similarly enter in the format: 'f x y'.\nTo clear the eight adjacent square around a tile, use 'u'.")
    print("To make your first move, enter 'u', then two coordinates x and y, separated by a space.")
    mine_makeboard.display(startBoard)
    finalBoard, minelist = startMove(height, length, mines, startBoard)
    mainGame()


def mainGame():
    global gameRunning, finalBoard, uncovered, flaglist, minelist
    while gameRunning:
        checkLoss()
        mine_makeboard.newdisplay(finalBoard, uncovered, flaglist)
        print("MINES LEFT:", (mines-len(flaglist)))
        turnIn = (input("\n>>> ")).split(" ")
        b, a = int(turnIn[1])-1, int(turnIn[2])-1

        if turnIn[0] == 'u':
            uncover(finalBoard, (a, b))
        elif turnIn[0] == "f":
            flag(finalBoard, (a, b))

        if len(uncovered) == (height*length)-mines:
            winning()

startGame()