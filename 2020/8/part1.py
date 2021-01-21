with open("vstup.txt", "r") as f:
    listA = [[x[0:3],int(x[4:])] for x in f.read().split("\n")]

counter = 0
acc = 0
lineList = []
print(listA)

while True:
    if lineList.count(counter) == 1:
        print(acc)
        break
    lineList.append(counter)
    print(listA[counter][0])
    if listA[counter][0] == "jmp":
        counter += listA[counter][1] - 1
    elif listA[counter][0] == "acc":
        acc +=listA[counter][1]
    counter +=1