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

for i in range(preambule, len(listA)):
    if not func():
        print(listA[i])
        break
    pStart+=1
