import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()

draws = lines[0].rstrip("\n").split(",")

#tables to arrays
boards = []
boardId = -1
row = 0

#boards -> 2D array with spaces inside
def formatBoards(boards):
    for board in boards:
        for row in board:
            for col in row:
                if col == "":
                    row.remove("")

def loadBoards(boards):
    for index, line in enumerate(lines):
        if index <= 0: continue

        if lines[index][0] == "\n":
            boards.append([])
            boardId += 1
            row = 0
            continue

        boards[boardId].append(lines[index].rstrip("\n").split(" "))
        row += 1

formatBoards(boards)
print(boards)