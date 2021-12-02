import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

horizontal = 0
depth = 0

inputFile = open(sys.argv[1], "r")
steps = inputFile.readlines()

#Formatting array
for index, step in enumerate(steps):
    steps[index] = int(step.rstrip("\n"))

