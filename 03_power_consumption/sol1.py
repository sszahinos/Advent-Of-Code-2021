import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

#############

inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()

#Array counting "ones" in each row's column
#-1 -> don't picking "\n"
count = [0] * (len(lines[0])-1)

gammaRate = ""
epsilonRate = ""

for index, line in enumerate(lines):
    #Formatting array
    lines[index] = line.rstrip("\n")
    
    #Iterating each column to count the "ones"
    for x in range(len(lines[index])):
        if lines[index][x] == "1":
            count[x] += 1
            

for col in count:
    if col >= int(len(lines)/2): # one is most common
        gammaRate += "1"
        epsilonRate += "0"
    else: # zero is most common
        gammaRate += "0"
        epsilonRate += "1"
    
gammaRateInt = int(gammaRate, 2)
epsilonRateInt = int(epsilonRate, 2)

print("Gamma: {}\nEpsilon: {}\n".format(gammaRate, epsilonRate))
print("Gamma(dec): {}\nEpsilon(dec): {}\n".format(gammaRateInt, epsilonRateInt))
print("Puzzle answer: {}".format(gammaRateInt * epsilonRateInt))
