from copy import deepcopy
with open("vstup.txt", "r") as f:
    listA = [list(x) for x in f.read().split("\n")]

rowLen = len(listA)
colLen = len(listA[0])

def recursion(lst):
    lst2 = deepcopy(lst)
    for row in range(rowLen):
        for col in range(colLen):
            counter = 0
            if lst[row][col] != '.':   
                for rowStep in [-1,0,1]:
                    for colStep in [-1,0,1]:
                        if not (rowStep == 0 and colStep ==0):
                            newR = row + rowStep
                            newC = col + colStep
                            if 0<=newR<rowLen and 0<=newC<colLen and lst[newR][newC] == '#':
                                counter += 1
                if lst[row][col] == 'L' and counter == 0:
                    lst2[row][col] = '#'
                elif lst[row][col] == '#' and counter >= 4:
                    lst2[row][col] = 'L'
    if lst2 != lst:
        recursion(lst2)
    else:
        ans = 0
        for line in lst2:
            ans+= line.count("#")
        print(ans)

recursion(listA)
        
