with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]
move = [1,3,5,7,1]
down = 1
position = 0
count = 0
countTemp = 1
for i in range(5):
    if i == 4:
        down = 2
    for e in range(0,len(listA),down):
        position = position%len(listA[0])
        if listA[e][position] == "#":
            count+=1
        position += move[i]
    countTemp *= count
    count =0
    position = 0
print(countTemp)
