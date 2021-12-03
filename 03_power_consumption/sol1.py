import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

FORWARD = "forward"
UP = "up"
DOWN = "down"

horizontal = 0
depth = 0

def goUp(distance):
    global depth
    depth -= distance

def goDown(distance):
    global depth
    depth += distance

def goForward(distance):
    global horizontal
    horizontal += distance

inputFile = open(sys.argv[1], "r")
steps = inputFile.readlines()

#Formatting array
for index, step in enumerate(steps):
    steps[index] = step.rstrip("\n")
    steps[index] = steps[index].split(" ")
    if steps[index][0] == FORWARD:
        goForward(int(steps[index][1]))
    elif steps[index][0] == UP:
        goUp(int(steps[index][1]))
    elif steps[index][0] == DOWN:
        goDown(int(steps[index][1]))

print("Distance: {}\nDepth: {}".format(horizontal, depth))
print("Puzzle answer: {}".format(horizontal*depth))
