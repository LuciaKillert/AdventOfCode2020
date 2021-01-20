with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]
count = 0
for line in listA:
    _letter = line.find(":")-1 
    _pomlcka = line.find("-")
    minN = int(line[:_pomlcka])
    maxN = int(line[_pomlcka+1:_letter-1])
    word = line[_letter+2:]
    if word.count(line[_letter]) >= minN and word.count(line[_letter]) <= maxN:
        count+= 1
print(count)
