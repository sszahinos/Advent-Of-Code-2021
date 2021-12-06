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

def drawLine(coord, grid):
    #x1y1 -> x2y2
    #6,4 -> 2,0
    #7,0 -> 7,4

    if (coord[0] > coord[2] or (coord[0] == coord[2] and coord[1] > coord[3])): #reverse (left to right and up to down)
        coord[0], coord[2] = coord[2], coord[0]
        coord[1], coord[3] = coord[3], coord[1]
    print(coord)

    while coord[0] != coord[2] or coord[1] != coord[3]:
        #print("GRID COORD: {}/{}".format(grid[coord[0]],coord[1]))
        if grid[coord[0]][coord[1]] == ".":
            grid[coord[0]][coord[1]] = 1
        else:
            grid[coord[0]][coord[1]] += 1

        if coord[0] != coord[2]:
            coord[0] += 1

        if coord[1] != coord[3] and coord[1] < coord[3]:
            coord[1] += 1
        elif coord[1] != coord[3] and coord[1] > coord[3]:
            coord[1] -= 1

    if grid[coord[2]][coord[3]] == ".":
        grid[coord[2]][coord[3]] = 1
    else:
        grid[coord[2]][coord[3]] += 1

    #print(grid)

def fillGrid(coords, grid):
    for coord in coords:
        drawLine(coord, grid)
    #print(grid)

grid = generateGrid(coords)
#print(grid)
fillGrid(coords, grid)
print(grid)

