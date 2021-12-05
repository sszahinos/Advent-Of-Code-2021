import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()

draws = []
boards = []
coord = []

def loadDraws():
    draws = lines[0].rstrip("\n").split(",")
    return draws

def loadBoards(boards):
    row = 0
    boardId = -1
    for index, line in enumerate(lines):
        if index <= 0: continue

        if lines[index][0] == "\n":
            boards.append([])
            boardId += 1
            row = 0
            continue

        boards[boardId].append(lines[index].rstrip("\n").split(" "))
        row += 1

    return boards

#boards -> 2D array with spaces inside
def formatBoards(boards):
    for board in boards:
        for row in board:
            for col in row:
                if col == "":
                    row.remove("")

#Returns the coord[row, col] of the found num
def findNum(board, draw): #ok
    coord = [-1, -1]
    for index1, row in enumerate(board):
        for index2, col in enumerate(row):
            if draw == col:
                coord = [index1, index2]
                break
    return coord

#Marks the found number with a X on the right
def markNum(board, coord): #ok
    board[coord[0]][coord[1]] += "X"
    

def checkRows(board): #ok
    #Check rows
    for row in board:
        for col in row:
            if col[-1] != "X":
                completed = False
                break
            else:
                completed = True
        if completed:
            return True

    return False

def checkColumns(board):
    #Check columns
    for col in range(len(board[0])):
        for row in board:
            if row[col][-1] != "X":
                completed = False
                break
            else:
                completed = True
        if completed:
            return True
    return False

def checkBoard(board):
    if checkRows(board) or checkColumns(board):
        return True
    return False

def getUnmarkedSum(board):
    sum = 0
    for row in board:
        for col in row:
            if col[-1] != "X":
                sum += int(col)
    return sum

def playBingo(boards, draws):
    for draw in draws:
        for board in boards:
            coord = findNum(board, draw)
            if coord[0] != -1: #Num found      
                markNum(board, coord)
                if checkBoard(board):
                    return getUnmarkedSum(board) * int(draw)
    return -1

draws = loadDraws()
loadBoards(boards)
formatBoards(boards)

finalScore = playBingo(boards, draws)
print("Final score: {}".format(finalScore))