def func():
    for num1 in listA[pStart:pStart + preambule]:
        for num2 in listA[pStart+1:pStart+preambule]:
            if num1 + num2 == listA[i]:
                return True
    return False

with open("vstup.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]

preambule = 25
pStart = 0
find = 0
findIndex = 0

for i in range(preambule, len(listA)):
    if not func():
        find = listA[i]
        findIndex = i
        break
    pStart+=1

summ = 0

for e in range(findIndex):
    summ += listA[e]
    for k in range(e+1,findIndex):
        summ += listA[k]
        if summ > find:
            summ = 0
            break
        elif summ == find:
            print(min(listA[e:k+1]) + max(listA[e:k+1]))