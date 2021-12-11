import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
inputs = inputFile.readlines()

for index, input in enumerate(inputs):
    inputs[index] = inputs[index].rstrip("\n").split(" | ")

#[ [ [input][code] ], [ [input2][code2] ], ...]
for index1, input in enumerate(inputs):
    for index2, part in enumerate(input):
        inputs[index1][index2] = inputs[index1][index2].split(" ")

###

CODES = [
    "abcefg", #0
    "cf", #1
    "acdeg", #2
    "acdfg", #3
    "bcdf", #4
    "abdfg", #5
    "abdefg", #6
    "acf", #7
    "abcdefg", #8
    "abcdfg" #9
]

UNIQUE_CODES_LENGTHS = [
    len(CODES[1]),
    len(CODES[4]),
    len(CODES[7]),
    len(CODES[8])
]

totalUniques = 0

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



for input in inputs:
    totalUniques += countUniques(input[1])

print("Total: {}".format(totalUniques))
