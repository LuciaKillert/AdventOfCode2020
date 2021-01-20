with open("vstup.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]
flag = False
for i in range(0,len(listA)):
    for e in range(1,len(listA)):
        for l in range(2,len(listA)):
            if listA[i] + listA[e] + listA[l] == 2020:
                print(listA[i]*listA[e]*listA[l])
                flag = True
                break
        if flag:
            break
    if flag:
        break