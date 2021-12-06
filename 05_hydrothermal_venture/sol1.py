import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
coords = inputFile.readlines()

#Format example: 0,9 -> 5,9 / 0,9,5,9 / [0,9,5,9]
for index, coord in enumerate(coords):
    coords[index] = coord.rstrip("\n").replace(" -> ", ",").split(",")
    
    for index2, value in enumerate(coords[index]):
        coords[index][index2] = int(value)

######

def generateGrid(coords):
    
    def getGreatestCoords(coords):
        greatestCoord = [0,0]
        for coord in coords:
            for index, value in enumerate(coord):
                if index % 2 == 0 and value > greatestCoord[0]:
                    greatestCoord[0] = value
                elif index % 2 != 0 and value > greatestCoord[1]:
                    greatestCoord[1] = value
        return greatestCoord

    grid = []
    maxDim = getGreatestCoords(coords)
    for row in range(maxDim[0]+1):
        grid.append([])
        for col in range(maxDim[1]+1):
            grid[row].append(".")
    return grid

def isStraight(coord):
    if coord[0] == coord[2] or coord[1] == coord[3]:
        return True
    else:
        return False

def drawLine(coord, grid):
    #x1y1 -> x2y2
    #6,4 -> 2,0
    #7,0 -> 7,4

    if (coord[0] > coord[2] or (coord[0] == coord[2] and coord[1] > coord[3])): #reverse (left to right and up to down)
        coord[0], coord[2] = coord[2], coord[0]
        coord[1], coord[3] = coord[3], coord[1]

    while coord[0] != coord[2] or coord[1] != coord[3]:
        if grid[coord[1]][coord[0]] == ".":
            grid[coord[1]][coord[0]] = 1
        else:
            grid[coord[1]][coord[0]] += 1

        if coord[0] != coord[2]:
            coord[0] += 1

        if coord[1] != coord[3] and coord[1] < coord[3]:
            coord[1] += 1
        elif coord[1] != coord[3] and coord[1] > coord[3]:
            coord[1] -= 1

    if grid[coord[3]][coord[2]] == ".":
        grid[coord[3]][coord[2]] = 1
    else:
        grid[coord[3]][coord[2]] += 1

def fillGrid(coords, grid):
    for coord in coords:
        if isStraight(coord):
            drawLine(coord, grid)

def countIntersections(grid):
    inters = 0
    for row in grid:
        for col in row:
            if col != "." and col != 1:
                inters += 1

    return inters

def printGrid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()

grid = generateGrid(coords)
fillGrid(coords, grid)
printGrid(grid)
print("Number of overlapping lines: {}".format(countIntersections(grid)))

