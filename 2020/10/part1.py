with open("vstup.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]

sortedList = sorted(listA)
#print(sortedList)
diffOne = 1
diffThree = 1

for i in range(len(sortedList)-1):
    if sortedList[i] + 1 == sortedList[i+1]:
        diffOne += 1
    elif sortedList[i] + 3 == sortedList[i+1]:
        diffThree += 1
print(diffOne*diffThree)