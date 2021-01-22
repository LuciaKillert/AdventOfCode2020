ans = []

def func(lst, g):
    global ans
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] > 3:
            return
    ans.append(lst[g-1:])
    #print("Adding: ", lst[g-1:])


with open("vstupTest.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]

sortedList = sorted(listA)
sortedList.insert(0, 0)
sortedList.append(sortedList[len(sortedList)-1]+3)
ans.append(sortedList)

counter = 0
tNum = 0

while counter< len(ans):
    #print("Testing: ", ans[counter])
    for i in range(1,len(ans[counter])-2):
        if i != 1:
            ans[counter].insert(i-1, tNum)
        tNum = ans[counter][i]
        ans[counter].pop(i)
        func(ans[counter], i)
    counter += 1

#print(ans)
print(len(ans))

for an in ans:
    print(an)
