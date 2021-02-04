L = [16,12,1,0,15,7,11]
index1 = 0
index2 = 0
current = 0

for i in range(len(L)-1,2020):
    current = L[i]
    if current not in L[:len(L)-1]:
        L.append(0)
    else:
        index1 = L[::-1].index(current)
        index2 = L[::-1].index(current,1)
        L.append(index2-index1)
    #print(L)
print(L[i])
