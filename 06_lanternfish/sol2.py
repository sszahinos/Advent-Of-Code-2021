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
DAYS = 256
NEW_FISH = 8
DEFAULT_FISH = 6

daysLeftFishes = []
dayChanges = []

def initializeChanges(changes):
    for index, change in enumerate(changes):
        changes[index] = 0

    return changes


def getTotalFishes(fishes):
    totalFishes = 0

    for fish in fishes:
        totalFishes += fish

    return totalFishes

###

for maxDays in range(NEW_FISH+1):
    daysLeftFishes.append(0)
    dayChanges.append(0)

for fish in fishes:
    daysLeftFishes[fish] += 1
daysLeftFishes = daysLeftFishes[::-1]
print("Initial: {}".format(daysLeftFishes))

for day in range(DAYS):
    for index, fishes in enumerate(daysLeftFishes): 
        if index != len(daysLeftFishes)-1 and fishes > 0: # > 0 days
            dayChanges[index+1] += fishes
            dayChanges[index] -= fishes
        elif fishes > 0: #0 days
            dayChanges[0] += fishes
            dayChanges[index] -= fishes
            dayChanges[-DEFAULT_FISH-1] += fishes

    #END DAY
    #Apply changes at the end of the day
    for index, fishes in enumerate(daysLeftFishes):
        daysLeftFishes[index] += dayChanges[index]
    #Reset changes
    initializeChanges(dayChanges)

print("Days: {}".format(DAYS))
print(daysLeftFishes)
print("Fish count: {}".format(getTotalFishes(daysLeftFishes)))

