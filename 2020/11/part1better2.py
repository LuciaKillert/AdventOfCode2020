import time
start = time.time()
with open("vstup.txt", "r") as f:
    listA = [list(x) for x in f.read().split("\n")]

listLen = len(listA)
rowLen = len(listA[0])

def change(lst):
    counter = 0
    j1 = False
    j2 = False
    i1 = False
    i3 = False
    lst2 = [ ["."] * (rowLen) for _ in range(listLen)]
    for i in range(listLen):
        for j in range(rowLen):
            #decide where to check for #
            if lst[i][j] == "L" or lst[i][j] == "#":
                if i == 0:
                    i3 = True
                elif i == listLen -1:
                    i1 = True              
                else:
                    i1 = True
                    i3 = True
                if j == 0:
                    j2 = True
                elif j == rowLen-1:
                    j1 = True
                else:
                    j1 = True
                    j2 = True
                #count all the #
                counter += lst[i][(j-1 if j1 else None):(j+2 if j2 else None)].count("#")
                if i1:
                    counter += lst[i-1][(j-1 if j1 else None):(j+2 if j2 else None)].count("#")
                if i3:
                    counter += lst[i+1][(j-1 if j1 else None):(j+2 if j2 else None)].count("#")
                #change seats if necessary
                if lst[i][j] == "L":
                    if counter == 0:
                        lst2[i][j] = "#"
                    else:
                        lst2[i][j] = "L"
                elif lst[i][j] == "#":
                    if counter > 4:
                        lst2[i][j] = "L"
                    else:
                        lst2[i][j] = "#"
            counter = 0
            j1 = False
            j2 = False
            i1 = False
            i3 = False
    if lst2 != lst:
        lst = lst2
        change(lst2)
    else:
        ans = 0
        for line in lst:
            ans+= line.count("#")
        print(ans)


change(listA)
print(time.time()-start)