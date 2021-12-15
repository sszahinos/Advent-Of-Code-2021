import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
inputs = inputFile.readlines()

for index, input in enumerate(inputs):
    inputs[index] = list(inputs[index].rstrip("\n"))
    for index2, data in enumerate(inputs[index]):
        inputs[index][index2] = int(data)

###

riskLevel = 0
lowPointFound = False

def addRiskLevel(toAdd):
    global riskLevel
    riskLevel += toAdd +1

def findRiskPoints(data):
    basins = []
    lowPointFound = False
    for rowIndex, row in enumerate(data):
        for colIndex, col in enumerate(row):
            if rowIndex == 0: #First row
                if (colIndex == 0 and 
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex == len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex != 0 and colIndex != len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True
                    
            elif rowIndex == len(data)-1:
                if (colIndex == 0 and
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex-1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex == len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex-1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex != 0 and colIndex != len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex-1][colIndex] > col):
                    lowPointFound = True
            else:
                if (colIndex == 0 and
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex-1][colIndex] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex == len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex-1][colIndex] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True
                elif (colIndex != 0 and colIndex != len(data[rowIndex])-1 and
                    data[rowIndex][colIndex-1] > col and
                    data[rowIndex][colIndex+1] > col and
                    data[rowIndex-1][colIndex] > col and
                    data[rowIndex+1][colIndex] > col):
                    lowPointFound = True

            if lowPointFound:
                basins.append([rowIndex, colIndex])
                lowPointFound = False

    return basins

def getRightSequence(data, coord):
    basinSize = 0
    for col in range(coord[1], len(data[0])-1):
        #print("comparing: {}/{}".format(data[coord[0]][col]+1, data[coord[0]][col+1]))
        if data[coord[0]][col]+1 == data[coord[0]][col+1]:
            basinSize += 1
        else:
            break

def getLeftSequence(data, coord):
    basinSize = 0
    for col in range(coord[1], 0, -1):
        if data[coord[0]][col]+1 == data[coord[0]][col-1]:
            basinSize += 1
        else:
            break

def getUpSequence(data, coord):
    #basinSize = 0
    #if data[data[0]][coord[1]]+1 == data[data[0]-1][coord[1]]:
    #    basinSize += 1
    #for row in range(coord[0], 0, -1):
        #if data[row][coord[1]]+1 == data[row-1][coord[1]]:
        #    basinSize += 1
     #   else:
      #      break
    return data[data[0]][coord[1]]+1 == data[data[0]-1][coord[1]]

def getDownSequence(data, coord):
    basinSize = 0
    for row in range(coord[0], len(data)-1):
        if data[row][coord[1]]+1 == data[row+1][coord[1]]:
            basinSize += 1
        else:
            break

def getBasinSize(data, basin):
    print(basin)
    #getRightSequence(data, basin[3])
    #getLeftSequence(data, basin[1])
    #getUpSequence(data, basin[3])
    getDownSequence(data, basin[1])

getBasinSize(inputs, findRiskPoints(inputs))