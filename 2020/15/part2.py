import time
start = time.time()
nums = [16,12,1,0,15,7,11]

L = {16:1,12:2,1:3,0:4,15:5,7:6,11:7}
F = {16:1,12:2,1:3,0:4,15:5,7:6,11:7}

diff = 0
current = nums[-1] #3,0

for i in range(len(L)+1,30000001): #4,5
    #print(current)
    if F[current] == L[current]:
        #print("just one")
        if 0 in L:
            F[0] = L[0]
        else:
            F[0] = i
        L[0] = i
        current = 0
    else:
        diff = L[current] - F[current]
        #print("diff:",diff, L[current], F[current])
        if diff not in L:
            L[diff] = i
            F[diff] = i
        else:
            F[diff] = L[diff]
            L[diff] = i
        current = diff 
print(current)
print(time.time()-start)
