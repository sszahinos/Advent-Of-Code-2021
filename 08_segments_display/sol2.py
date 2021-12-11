import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
inputs = inputFile.readlines()

for index, input in enumerate(inputs):
    inputs[index] = inputs[index].rstrip("\n").split(" | ")

#[ [ [input1, input2...][code1, code2] ], ...] -> sorted
#
for index1, input in enumerate(inputs):
    for index2, part in enumerate(input):
        inputs[index1][index2] = inputs[index1][index2].split(" ")
        for index3, code in  enumerate(inputs[index1][index2]):
            inputs[index1][index2][index3] = "".join(sorted(inputs[index1][index2][index3]))
###

CODES = [
    "abcefg", #0 / 6
    "cf", #1- / 2
    "acdeg", #2 / 5
    "acdfg", #3 / 5
    "bcdf", #4- / 4
    "abdfg", #5 / 5
    "abdefg", #6 / 6
    "acf", #7- / 3
    "abcdefg", #8- / 7
    "abcdfg" #9 / 6
]

UNIQUE_CODES_LENGTHS = [
    len(CODES[1]), #1
    len(CODES[4]), #4
    len(CODES[7]), #7
    len(CODES[8])  #8
]

####

newCode = [ #It will change with each code
    "X", #0
    "X", #1
    "X", #2
    "X", #3
    "X", #4
    "X", #5
    "X", #6
    "X", #7
    "X", #8
    "X" #9 and full pattern
]

def initializePattern():
    for index, pattern in enumerate(newCode):
        newCode[index] = "X"

def countUniques(codes):
    count = 0
    for code in codes:
        if isUnique(code):
            count += 1
    return count

def isUnique(code):
    result = False
    if len(code) in UNIQUE_CODES_LENGTHS:
        result = True
    return result

def findUnique(code):
    if isUnique(code):
        if len(code) == UNIQUE_CODES_LENGTHS[0]:
            newCode[1]  = code
        elif len(code) == UNIQUE_CODES_LENGTHS[1]:
            newCode[4] = code
        elif len(code) == UNIQUE_CODES_LENGTHS[2]:
            newCode[7] = code
        elif len(code) == UNIQUE_CODES_LENGTHS[3]: #redundant
            newCode[8] = code

    
def getPattern(codes):
    for code in codes:
        findUnique(code)

def getConcurrences(code, num):
    concurrences = 0
    for letter in code:
        if letter in sorted(newCode[num]):
            concurrences += 1

    return concurrences

def fillPattern(codes):
    for code in codes:
        if len(code) == 6: #0, 6 and 9      
            if getConcurrences(code, 1) == 1:
                newCode[6] = code #6
            elif getConcurrences(code, 4) == 3:
                newCode[0] = code #0
            else:
                newCode[9] = code #9

        elif len(code) == 5: #2, 3 and 5
            if getConcurrences(code, 1) == 2:
                newCode[3] = code #3
            elif getConcurrences(code, 4) == 2:
                newCode[2] = code #2
            else:
                newCode[5] = code #5
            
def decode(codes):
    number = ""
    for code in codes:
        for index, pattern in enumerate(newCode):
            if code == pattern:
                number += "{}".format(index)
                break

    return int(number)

                
        

totalSum = 0

for input in inputs:
    
    getPattern(input[0])
    fillPattern(input[0])
    totalSum += decode(input[1])
    initializePattern()

print("Total sum of codes: {}".format(totalSum))

