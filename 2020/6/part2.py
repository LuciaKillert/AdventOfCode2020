with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n\n")]

listB = []
listAnswers = []
summ = 0

for group in listA:
    num = group.count("\n")
    listB = group.replace("\n", "")
    for letter in listB:
        if listB.count(letter) > num and letter not in listAnswers:
            listAnswers.append(letter)
    summ += len(listAnswers)
    listAnswers.clear()
print(summ)