import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
inputs = inputFile.readlines()

for index, input in enumerate(inputs):
    inputs[index] = inputs[index].rstrip("\n").split(" | ")
