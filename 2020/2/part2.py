with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]
count = 0
for line in listA:
    _letter = line.find(":")-1 
    _pomlcka = line.find("-")
    first = int(line[:_pomlcka])
    second = int(line[_pomlcka+1:_letter-1])
    word = line[_letter+3:]
    print(word)
    if word[first-1] == line[_letter] and word[second-1] != line[_letter]:
        count+=1
    elif word[first-1] != line[_letter] and word[second-1] == line[_letter]:
        count+=1
print(count)
