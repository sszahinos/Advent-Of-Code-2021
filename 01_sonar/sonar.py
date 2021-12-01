import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

inputFile = open(sys.argv[1], "r")
measures = inputFile.readlines()
#Formatting array
for index, measure in enumerate(measures):
    measures[index] = int(measure.rstrip("\n"))

auxPre = 0
incCount = -1
decCount = 0

sumPre = 0

for index, measure in enumerate(measures):
    if int(measure.rstrip("\n")) + int(measures[index+1].rstrip("\n"))> auxPre:
        incCount += 1
    else:
        decCount += 1
    
    auxPre = int(measure)

print("Increased: {} / Decreased: {}".format(incCount, decCount))
    
        

