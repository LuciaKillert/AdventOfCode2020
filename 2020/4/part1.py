with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n\n")]
valid = 0
listB = []
for person in listA:
    if person.count(":") == 8 or (person.count(":") == 7 and person.find("cid") == -1):
        valid+=1
print(valid)

