from copy import deepcopy
L = []
with open("vstup.txt", "r") as f:
    L.append([list(x) for x in f.read().splitlines()])

#print(L)

G = []
G.append(L)
#print(G)

for r in range(6):
    for g in G:
        for l in g:
            l.insert(0, ['.' for _ in range(len(l[0]))])
            l.append(['.' for _ in range(len(l[0]))])
            for k in l:
                k.insert(0, '.')
                k.append('.')
        g.insert(0, [['.' for _ in range(len(g[0][0]))] for _ in range(len(g[0]))])
        g.append([['.' for _ in range(len(g[0][0]))] for _ in range(len(g[0]))])
    G.insert( 0, [   [   [   '.' for _ in range(len(G[0][0][0]))   ] for _ in range(len(G[0][0]))   ] for _ in range(len(G[0]))   ]   )
    G.append(   [   [   [   '.' for _ in range(len(G[0][0][0]))   ] for _ in range(len(G[0][0]))   ] for _ in range(len(G[0]))   ]   )
    K = deepcopy(G)
    for numW,w in enumerate(G):
        for numZ,z in enumerate(w):
            for numY,y in enumerate(z):
                for numX,x in enumerate(y):
                    counter = 0
                    for dw in [-1,0,1]:
                        newW = numW + dw
                        for dz in [-1,0,1]:
                            newZ = numZ + dz
                            for dy in [-1,0,1]:
                                newY = numY + dy
                                for dx in [-1,0,1]:
                                    if dz == dy == dx == dw == 0:
                                        continue
                                    newX = numX + dx
                                    if 0<=newW<len(G) and 0<=newZ < len(w) and 0<=newY < len(z) and 0<=newX < len(y) and G[newW][newZ][newY][newX] == '#':
                                        counter += 1
                    if G[numW][numZ][numY][numX] == '#' and not(1<counter<4):
                        K[numW][numZ][numY][numX] = '.'
                    elif G[numW][numZ][numY][numX] == '.' and counter == 3:
                        K[numW][numZ][numY][numX] = '#'
    G = deepcopy(K)

ans = 0
for g in G:
    for l in g:
        for k in l:
            #print(k)
            ans += k.count('#')
        #print("#######")
print(ans)