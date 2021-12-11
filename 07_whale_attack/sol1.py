import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
crabs = inputFile.readlines()[0].split(",")
for index, item in enumerate(crabs):
    crabs[index] = int(item)

minFuel = None
minPos = None

for pos in crabs:
    fuel = 0
    for crab in crabs:
        fuel += abs(crab-pos)
    
    if minFuel == None or fuel < minFuel:
        minFuel = fuel
        minPos = pos

print("Position: {} Fuel: {}".format(minPos, minFuel))