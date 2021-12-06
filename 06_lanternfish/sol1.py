import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
fishes = inputFile.readlines()[0].split(",")
for index, item in enumerate(fishes):
    fishes[index] = int(item)

###
DAYS = 80
NEW_FISH = 8
DEFAULT_FISH = 6

for day in range(DAYS):
    fishesToAdd = 0

    for index, fish in enumerate(fishes):
        if fish == 0:
            #New fish
            fishesToAdd += 1
            #Reset old
            fishes[index] = DEFAULT_FISH
        else:
            fishes[index] -= 1
    
    for newFishes in range(fishesToAdd):
        fishes.append(NEW_FISH)

print("Days passed: {}".format(DAYS))
print("Fish count: {}".format(len(fishes)))

