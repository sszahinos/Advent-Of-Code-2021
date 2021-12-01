import sys

if len(sys.argv) != 2:
    print("Error: Pass one input file as argument.")
    sys.exit()

inputFile = open(sys.argv[1], "r")
measures = inputFile.readlines()
#Formatting array
for index, measure in enumerate(measures):
    measures[index] = int(measure.rstrip("\n"))

incCount = -1
decCount = 0

sumPre = 0

for index, measure in enumerate(measures):
    #The first and last item doesn't have 3 items to sum -> skip
    if index == 0:
        continue
    elif index == len(measures)-1:
        break

    sum = measure + measures[index+1] + measures[index-1]
    if sum > sumPre:
        incCount += 1
    elif sum < sumPre:
        decCount += 1
    
    sumPre = sum

print("Increased: {} / Decreased: {}".format(incCount, decCount))
    
        

