
with open("vstup.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]

sortedList = sorted(listA)
sortedList.insert(0, 0)
sortedList.append(sortedList[len(sortedList)-1]+3)

DP = {}

def recursion(i):
    ans = 0
    if i == len(sortedList)-1:
        return 1
    elif i in DP:
        return DP[i]
    for j in range(i+1, len(sortedList)):
        if sortedList[j] - sortedList[i] <= 3:
            ans += recursion(j)
    DP[i] = ans
    return ans

print(recursion(0))
