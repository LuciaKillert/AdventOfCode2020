with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]
move = 7
position = 0
count = 0
for line in listA:
    position = position%len(line)
    if line[position] == "#":
        count+=1
    position += move
print(count)
