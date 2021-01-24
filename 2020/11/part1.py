import time 
start = time.time()
with open("vstup.txt", "r") as f:
    listA = [list(x) for x in f.read().split("\n")]

listLen = len(listA)
rowLen = len(listA[0])

def change(lst):
    counter = 0
    lst2 = [ ["."] * (rowLen) for _ in range(listLen)]
    for i in range(listLen):
        for j in range(rowLen):
            if lst[i][j] == "L" or lst[i][j] == "#":
                #check and calculate all the #
                if i == 0:
                    if j == 0:
                        counter += lst[i][: j+2].count("#")
                        counter += lst[i+1][: j+2].count("#")
                    elif j == rowLen-1:
                        counter += lst[i][j-1:].count("#")
                        counter += lst[i+1][j-1:].count("#")
                    else:
                        counter += lst[i][j-1: j+2].count("#")
                        counter += lst[i+1][j-1: j+2].count("#")
                elif i == listLen -1:
                    if j == 0:
                        counter += lst[i][: j+2].count("#")
                        counter += lst[i-1][: j+2].count("#")
                    elif j == rowLen-1:
                        counter += lst[i][j-1:].count("#")
                        counter += lst[i-1][j-1:].count("#")
                    else:
                        counter += lst[i][j-1: j+2].count("#")
                        counter += lst[i-1][j-1: j+2].count("#")
                else:
                    if j == 0:
                        counter += lst[i][: j+2].count("#")
                        counter += lst[i+1][: j+2].count("#")
                        counter += lst[i-1][: j+2].count("#")
                    elif j == rowLen-1:
                        counter += lst[i][j-1:].count("#")
                        counter += lst[i-1][j-1:].count("#")
                        counter += lst[i+1][j-1:].count("#")
                    else:
                        counter += lst[i][j-1: j+2].count("#")
                        counter += lst[i-1][j-1: j+2].count("#")
                        counter += lst[i+1][j-1: j+2].count("#")

                #decide whether to change it
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
    if lst2 != lst:
        lst = lst2
        change(lst2)
    else:
        ans = 0
        for line in lst:
            ans+= line.count("#")
        print(ans)


change(listA)
print(time.time() - start)