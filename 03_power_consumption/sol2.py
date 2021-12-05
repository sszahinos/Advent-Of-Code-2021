import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
for index, line in enumerate(lines):
    #Formatting array
    lines[index] = line.rstrip("\n")

def checkBits(data, col):
    bitOnes = 0
    bitZeroes = 0

    result = 2

    #Counting col's bit in all lines
    for index, line in enumerate(data):
        if data[index][col] == "1":
            bitOnes += 1
        else:
            bitZeroes += 1

    if bitOnes > bitZeroes:
        result = "1"
    elif bitOnes < bitZeroes:
        result = "0"
    else:
        result = "-1"
    
    return result

def filterLines(data, result, col):
    newArr1 = []
    for line in data:
        if line[col] == result:
            newArr1.append(line)

    return newArr1

#mode = "ox" / mode = "co2". default mode = co2
def getRatingResult(mode):
    global lines
    ratingArr = lines
    
    repeatedNum = 0
    for col in range(len(ratingArr[0])):

        if len(ratingArr) == 1:
            break

        repeatedNum = checkBits(ratingArr, col)

        if mode == "ox":
            if repeatedNum == "-1":                    
                ratingArr = filterLines(ratingArr, "1", col)
            else:
                ratingArr = filterLines(ratingArr, repeatedNum, col)
        else:
            if repeatedNum == "-1" or repeatedNum == "1":                    
                ratingArr = filterLines(ratingArr, "0", col)
            else:
                ratingArr = filterLines(ratingArr, "1", col)

    return ratingArr[0]

ox = getRatingResult("ox")
co2 = getRatingResult("co2")

print("Oxygen generator rating: {}\nCO2 scrubber rating: {}\n"
    .format(ox, co2))
print("Life support rating: {}\n".format(int(ox,2) * int(co2,2)))
