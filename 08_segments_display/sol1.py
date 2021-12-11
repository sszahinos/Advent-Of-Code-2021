import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
inputs = inputFile.readlines()

for index, input in enumerate(inputs):
    inputs[index] = inputs[index].rstrip("\n").split(" | ")

#[[input][code], ...]
for index1, input in enumerate(inputs):
    for index2, part in enumerate(input):
        inputs[index1][index2] = inputs[index1][index2].split(" ")

###

