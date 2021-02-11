from copy import deepcopy
L = []
with open("vstup.txt", "r") as f:
    L.append([list(x) for x in f.read().splitlines()])

#print(L)


for r in range(6):
    for l in L:
        l.insert(0, ['.' for _ in range(len(l[0]))])
        l.append(['.' for _ in range(len(l[0]))])
        for k in l:
            k.insert(0, '.')
            k.append('.')
    L.insert(0, [['.' for _ in range(len(L[0][0]))] for _ in range(len(L[0]))])
    L.append([['.' for _ in range(len(L[0][0]))] for _ in range(len(L[0]))])
    #for l in L:
    #    for k in l:
    #        print(k)
    #    print("#######")
    K = deepcopy(L)
    for numZ,z in enumerate(L):
        for numY,y in enumerate(z):
            for numX,x in enumerate(y):
                counter = 0
                for dz in [-1,0,1]:
                    newZ = numZ + dz
                    for dy in [-1,0,1]:
                        newY = numY + dy
                        for dx in [-1,0,1]:
                            if dz == dy == dx == 0:
                                continue
                            newX = numX + dx
                            if 0<=newZ < len(L) and 0<=newY < len(z) and 0<=newX < len(y) and L[newZ][newY][newX] == '#':
                                counter += 1
                if L[numZ][numY][numX] == '#' and not(1<counter<4):
                    K[numZ][numY][numX] = '.'
                elif L[numZ][numY][numX] == '.' and counter == 3:
                    K[numZ][numY][numX] = '#'
    L = deepcopy(K)

ans = 0
for l in L:
    for k in l:
        #print(k)
        ans += k.count('#')
    #print("#######")
print(ans)