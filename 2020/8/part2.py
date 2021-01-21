with open("vstup.txt", "r") as f:
    listA = [[x[0:3],int(x[4:])] for x in f.read().split("\n")]

counter = 0
acc = 0
lineList = []
listLen = len(listA)
wrongList = []
done = False

while True:
        if lineList.count(counter) == 1:
            break
        lineList.append(counter)
        if listA[counter][0] == "jmp":
            wrongList.append(counter)
            counter += listA[counter][1] - 1
        elif listA[counter][0] == "acc":
            acc +=listA[counter][1]
        else:
            wrongList.append(counter)
        counter +=1
tempInstruction = ""
tempCounter = 0

for i in wrongList:
    counter = 0
    acc = 0
    lineList = []
    if i != wrongList[0]:
        listA[tempCounter][0] = tempInstruction
    tempInstruction = listA[i][0]
    tempCounter = i

    if tempInstruction == "jmp":
        listA[i][0] = "nop"
    else:
        listA[i][0] = "jmp"

    while True:
        if lineList.count(counter) == 1:
            break
        elif counter >= listLen:
            print(acc)
            break
        lineList.append(counter)
        if listA[counter][0] == "jmp":
            counter += listA[counter][1] - 1
        elif listA[counter][0] == "acc":
            acc +=listA[counter][1]
        counter +=1
    