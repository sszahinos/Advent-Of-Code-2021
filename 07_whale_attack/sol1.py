import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
fishes = inputFile.readlines()[0].split(",")
for index, item in enumerate(fishes):
    fishes[index] = int(item)