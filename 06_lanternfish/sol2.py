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
DAYS = 5
NEW_FISH = 8
DEFAULT_FISH = 6

daysLeftFishes = []
for maxDays in range(NEW_FISH+1):
    daysLeftFishes.append(0)

for fish in fishes:
    daysLeftFishes[fish] += 1
print("Initial: {}".format(daysLeftFishes))

for day in range(DAYS):
    for index, fishes in enumerate(reversed(daysLeftFishes)):
        if daysLeftFishes[index] != 0:
            print("PRE {}".format(fishes))
            daysLeftFishes[index] -= 1
            print("post {}".format(daysLeftFishes[index]))

        if daysLeftFishes[index] != 0 and index != len(daysLeftFishes)-1:
            daysLeftFishes[index+1] += 1
        elif daysLeftFishes[index] != 0 and index == len(daysLeftFishes)-1: #0
            daysLeftFishes[len(daysLeftFishes)-1] += 1

    print(daysLeftFishes)
            
        





    #fishesToAdd = 0
    #for index, fish in enumerate(fishes):
    #    if fish == 0:
            #New fish
            #fishesToAdd += 1
            #Reset old
    #        fishes[index] = DEFAULT_FISH
    #    else:
    #        fishes[index] -= 1
    
    #for newFishes in range(fishesToAdd):
        #fishes.append(NEW_FISH)

#print("Days: {}".format(day))
#print("Fish count: {}".format(totalFishes))

