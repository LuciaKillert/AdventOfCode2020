with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n\n")]

listB = []
listAnswers = []
summ = 0

for group in listA:
    listB = group.replace("\n", "")
    for letter in listB:
        if letter not in listAnswers:
            listAnswers.append(letter)
    summ += len(listAnswers)
    listAnswers.clear()
print(summ)