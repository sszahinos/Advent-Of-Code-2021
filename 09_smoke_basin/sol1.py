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
    
for rowIndex, row in enumerate(inputs):
    for colIndex, col in enumerate(row):
        if rowIndex == 0: #First row
            if (colIndex == 0 and 
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True
            elif (colIndex == len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True
            elif (colIndex != 0 and colIndex != len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True
                
        elif rowIndex == len(inputs)-1:
            if (colIndex == 0 and
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex-1][colIndex] > col):
                lowPointFound = True
            elif (colIndex == len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex-1][colIndex] > col):
                lowPointFound = True
            elif (colIndex != 0 and colIndex != len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex-1][colIndex] > col):
                lowPointFound = True
        else:
            if (colIndex == 0 and
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex-1][colIndex] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True
            elif (colIndex == len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex-1][colIndex] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True
            elif (colIndex != 0 and colIndex != len(inputs[rowIndex])-1 and
                inputs[rowIndex][colIndex-1] > col and
                inputs[rowIndex][colIndex+1] > col and
                inputs[rowIndex-1][colIndex] > col and
                inputs[rowIndex+1][colIndex] > col):
                lowPointFound = True

        if lowPointFound:
            addRiskLevel(col)
            lowPointFound = False

print("Risk level: {}".format(riskLevel))