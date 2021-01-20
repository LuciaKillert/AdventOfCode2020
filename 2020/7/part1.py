with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]

listColors = ["shiny gold"]

def finder(color):
    global listColors
    for line in listA:
        if line.find(color, line.find("contain")) != -1:
            listColors.append(line[:line.find("bag")-1])

for i in listColors:
    finder(i)
print(len(set(listColors))-1)