with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]

result = 0
row = 0
IDs = []

def findID(minN, maxN, letter, line):
    global row
    middle = (minN + maxN)/2 
    if isinstance(middle, float):
        if line[letter] == "B" or line[letter] == "R":
            minN = middle +.5
        else:
            maxN = middle -.5
    elif line[letter] == "B" or line[letter] == "R":
        minN = middle
    else:
        maxN = middle
    if minN == maxN:
        if letter == 6:
            row = maxN
            findID(0,7,letter+1, line)
        else:
            IDs.append((row*8)+minN)
    else:
        findID(minN, maxN, letter+1, line)

for line in listA:
    findID(0,127,0, line)
for num in IDs:
    if num > result:
        result = num
print(int(result))
    