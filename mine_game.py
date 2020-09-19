import mine_makeboard, minetest, copy, sys

# uncovered, flaglist, finalBoard = [], [], []
# height, length, mines = 0, 0, 0
# gameRunning = True

def getInput():
    """Gets input of dimensions and mines of game board."""
    # validating user input
    accepted = False
    while not accepted:
        try:
            boardHeight = int(input("Enter board height:\t"))
            boardLength = int(input("Enter board length:\t"))
            mineInput = int(input("Enter amount of mines:\t"))
            assert boardHeight > 0 and boardLength > 0 and mineInput > 1
            assert mineInput < boardLength * boardHeight
            accepted = True
        except Exception:
            print("Please enter positive integer dimensions and mines such that 1 < mines < length*height.\n")

    return boardHeight, boardLength, mineInput

def hideboard(board):
    hidden = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            hidden[i][j] = "[]"
    
    return hidden

def startMove(uncovered, height, length, mines, board):
    move = [(int(i)-1) for i in ((input("Coordinates \"x y\" >>>\t")).split(" "))[1:]]
    b, a = move
    surList = mine_makeboard.locSurround(a, b, board)[2]

    finBoard, minelist = mine_makeboard.makeboard(height, length, mines, surList)
    uncovered += minetest.auxG(finBoard, (a, b))
    return finBoard, minelist

def uncover(uncovered, flaglist, board, pos):
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

def flag(flaglist, uncovered, board, pos):
    if pos in uncovered:
        print("\nYou cannot flag an uncovered square.\n")
    elif pos in flaglist:
        flaglist.remove(pos)
    else:
        flaglist += [pos]

def checkLoss(uncovered, minelist):
    """Checks if game is lost (if user uncovered mine)."""
    for unc_tile in uncovered:
        if unc_tile in minelist:
            print("\n\n\nBOOM! You lost! :(\n\n\n")
            input("Press any key to exit...")
            gameRunning = False
            sys.exit()
    return 0    

def winning(gameRunning, flaglist, uncovered, minelist, finalBoard):
    flaglist = minelist
    mine_makeboard.newdisplay(finalBoard, uncovered, flaglist)
    print("\n\n\nYou win!\n\n\n")
    input("Press any key to exit...")
    sys.exit()

def startGame():
    print("\nWelcome to Pysweeper!\nTo uncover a tile, enter a 'u' for uncover, then x and y coordinates ('u x y')\n")
    print("To flag, similarly enter in the format: 'f x y'.\nTo clear the eight adjacent square around a tile, use 'u'.")
    print("To make your first move, enter 'u', then two coordinates x and y, separated by a space.\n\n")
    print("Firstly, enter the board dimensions:\n")
    uncovered, flaglist = [], []
    height, length, mines = getInput()
    initBoard = mine_makeboard.initboard(height, length)
    startBoard = hideboard(initBoard)
    mine_makeboard.display(startBoard)
    finalBoard, minelist = startMove(uncovered, height, length, mines, startBoard)
    mainGame(True, finalBoard, uncovered, flaglist, minelist, mines)


def mainGame(gameRunning, finalBoard, uncovered, flaglist, minelist, mines):
    while gameRunning:
        mine_makeboard.newdisplay(finalBoard, uncovered, flaglist)
        checkLoss(uncovered, minelist)
        print("MINES LEFT:", (mines-len(flaglist)))
        
        # validating user input
        accepted = False
        while not accepted:
            try:
                turnIn = (input("\n>>> ")).split(" ")
                b, a = int(turnIn[1])-1, int(turnIn[2])-1
                assert turnIn[0] in ['u', 'f']
                assert a < len(finalBoard) and b < len(finalBoard[0])
                accepted = True
            except Exception:
                print("Please enter a letter for uncovering/flagging (u, f) and coordinates,\nall separated by a space, within the board's dimensions. E.g. '>>> u 7 2'")

        if turnIn[0] == 'u':
            uncover(uncovered, flaglist, finalBoard, (a, b))
        elif turnIn[0] == "f":
            flag(flaglist, uncovered, finalBoard, (a, b))

        if len(uncovered) == (len(finalBoard)*len(finalBoard[0]))-mines:
            winning(gameRunning, flaglist, uncovered, minelist, finalBoard)

if __name__ == "__main__":
    startGame()