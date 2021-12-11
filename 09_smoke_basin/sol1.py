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
        lowPointFound = False
        if colIndex == 0: #first col
            if ((rowIndex == 0 and #first row
                    inputs[rowIndex][colIndex+1] > col and
                    inputs[rowIndex+1][colIndex] > col) or  
                (rowIndex == len(inputs)-1 and #Last row
                    inputs[rowIndex][colIndex+1] > col and
                    inputs[rowIndex-1][colIndex] > col) or 
                (inputs[rowIndex-1][colIndex] > col and #mid row
                    inputs[rowIndex+1][colIndex] > col and
                    inputs[rowIndex][colIndex+1] > col)): 
                lowPointFound = True
        
        elif colIndex == len(inputs[row])-1: #Last col
            if ((rowIndex == 0 and #first row
                    inputs[rowIndex][colIndex-1] > col and
                    inputs[rowIndex+1][colIndex] > col) or  
                (rowIndex == len(inputs)-1 and #Last row
                    inputs[rowIndex][colIndex-1] > col and
                    inputs[rowIndex-1][colIndex] > col) or 
                (inputs[rowIndex-1][colIndex] > col and #mid row
                    inputs[rowIndex+1][colIndex] > col and
                    inputs[rowIndex][colIndex-1] > col)): 
                lowPointFound = True
        else: #Mid col ##########REVISAR###########
            if ((rowIndex == 0 and #first row
                    inputs[rowIndex][colIndex-1] > col and
                    inputs[rowIndex+1][colIndex] > col) or  
                (rowIndex == len(inputs)-1 and #Last row
                    inputs[rowIndex][colIndex-1] > col and
                    inputs[rowIndex-1][colIndex] > col) or 
                (inputs[rowIndex-1][colIndex] > col and #mid row
                    inputs[rowIndex+1][colIndex] > col and
                    inputs[rowIndex][colIndex-1] > col)): 
                lowPointFound = True

        if lowPointFound:
            addRiskLevel(col)