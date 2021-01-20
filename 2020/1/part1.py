with open("vstup.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]
flag = False
for i in range(0,len(listA)):
    for e in range(1,len(listA)):
        if listA[i] + listA[e] == 2020:
            print(listA[i]*listA[e])
            flag = True
    if flag:
        break
