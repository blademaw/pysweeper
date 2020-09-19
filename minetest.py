def getOthers(a, b, board):
    oA, oB = a, b
    a, b = a-1, b-1
    res, coords = [], []
    for loc in range(9):
        if not(a < 0 or b < 0):
            try:
                if not(a == oA and b == oB):
                    res += [board[a][b]]
                    coords += [(a, b)]
            except IndexError:
                pass
        b += 1
        if (loc+1) % 3 == 0:
            a, b = a + 1, b - 3

    return res, coords

def getExpands(board, pos, around, coords, unc):
    notFound = True
    while notFound:
        notFound = False
        for i in range(len(unc)):
            a, b = unc[i]
            if board[a][b] == 0:
                around, coords = getOthers(a, b, board)
                for x in range(len(around)):
                    if coords[x] != 'M' and coords[x] not in unc:
                        notFound = True
                        unc.append(coords[x])
    return unc

def auxG(board, pos):
    unc = []
    unc += [pos]
    a, b = pos
    return sorted(getExpands(board, pos, getOthers(a, b, board)[0], getOthers(a, b, board)[1], unc))


# myB = [ [0, 0, 0, 0],
#         [0, 'M', 0, 'M']]

# print(auxG(myB, (0, 0)))