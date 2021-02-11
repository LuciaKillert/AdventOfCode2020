with open("vstup.txt", "r") as f:
    L = ["".join(x.split()) for x in f.read().splitlines()]

#print(L)


def findAns_r(lst):
    rNum = rCurr = curr = num = next = 0

    if lst[0].isdigit():
        num = int(lst[0])
        curr = 1

    elif lst[0] == '(':
        rNum, rCurr = findAns_r(lst[1:])
        num = rNum
        curr += rCurr + 2

    while curr < len(lst):
        next = curr + 1
        if lst[curr] == '+':
            if lst[next].isdigit():
                num += int(lst[next])
                curr += 2

            elif lst[next] == '(':
                rNum, rCurr = findAns_r(lst[next+1:]) #recursion
                num += rNum
                curr += rCurr + 3

        elif lst[curr] == '*':
            if lst[next].isdigit():
                num *= int(lst[next])
                curr += 2

            elif lst[next] == '(':
                rNum, rCurr = findAns_r(lst[next+1:]) #recursion
                curr += rCurr + 3
                num *= rNum

        elif lst[curr] == ')':
            return num, curr
    return num, curr

ans = []
for l in L:
    lineAns = findAns_r(l)[0]
    ans.append(lineAns)
print("SUM: ",sum(ans))
assert sum(ans) == 8298263963837