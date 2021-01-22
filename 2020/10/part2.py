ans = []

def func(lst):
    global ans
    for i in range(len(lst)-1):
        if not(lst[i] + 1 == lst[i+1] or lst[i] + 2 == lst[i+1] or lst[i] + 3 == lst[i+1]):
            return False
    if lst not in ans:
        ans.append(lst)
    return True

def func2(k):
    sList = sortedList.copy()
    while True:
        if k < len(sortedList)-2:
                stack.append(sList.pop(k+1))
                print(sList)
                if not func(sList):
                    sList.insert(k+1, stack.pop())
                    k+=1
        elif len(stack) != 0:
            t = sortedList.index(stack[len(stack)-1])
            g = stack.pop()
            sList.insert(t-len(stack), g)
            k = sList.index(g)
        else:
            break

with open("vstupTest.txt", "r") as f:
    listA = [int(x) for x in f.read().split("\n")]

sortedList = sorted(listA)
sortedList.insert(0, 0)
sortedList.append(sortedList[len(sortedList)-1]+3)


sList = []
stack = []

for i in range(len(sortedList)):
    stack.clear()
    func2(i)
    print("                       ")
print(len(ans))