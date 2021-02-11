import time 
start = time.time()
with open("vstup.txt", "r") as f:
    L = ["".join(x.split()) for x in f.read().splitlines()]



def findAns_r(lst):
    newL = []
    num = rNum = rCurr = curr = next = 0
    if lst[0].isdigit():
        num = int(lst[0])
        curr = 1

    elif lst[0] == '(':
        num, rCurr = findAns_r(lst[1:]) #recursion
        curr = rCurr + 2 # first and last parenthesis

    while curr < len(lst):

        next = curr +1
        if lst[curr] == '+':

            if lst[next].isdigit():
                num += int(lst[next])
            else: # '('
                rNum, rCurr = findAns_r(lst[curr+2:]) #recursion
                num += rNum
                curr += rCurr + 1

        elif lst[curr] == '*':
            newL.append(str(num))
            newL.append('*')

            if lst[next].isdigit():
                num = int(lst[next])

            else: # '('
                num, rCurr = findAns_r(lst[curr+2:]) #recursion
                curr += rCurr + 1

        elif lst[curr] == ')':
            newL.append(str(num))
            ans = 1

            for n in newL:
                if n != '*':
                    ans*=int(n)
            return ans, curr
        curr += 2


    newL.append(str(num)) # to keep it all in strings
    ans = 1
    for n in newL:
        if n != '*':
            ans*=int(n)
    return ans, curr

ans = []
for line in L:
    lineAns = findAns_r(line)[0]
    ans.append(lineAns)
print("SUM:",sum(ans))
print(time.time() - start)
assert sum(ans) == 145575710203332