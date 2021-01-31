with open("vstup.txt", "r") as f:
    L = [x for x in f.read().splitlines()]

mask = ''
mem = {}
val = 0
add = []
temp = 0

def change(ad, k):
    if ad not in add:
        for i in range(k+1,36):
            if mask[i] == 'X':
                ad[i] = '0'
                change(ad,i)
                ad[i] = '1'
                change(ad,i)
                break
            elif mask[i] == '1' and ad[i] != '1':
                ad[i] = '1'
        add.append(''.join(ad))

for line in L:
    if line.startswith("mask"):
        mask = line[7:]
        #print(mask)
    else:
        val = line[line.index('=')+2:]
        temp = bin(int(line[4:line.index(']')]))[2:]
        temp = list('0'*(36-len(temp)) + temp)
        #print(''.join(add), val)
        change(temp,0)
        for l in set(add):
            #print(int(l,2), val)
            mem[int(l,2)] = val
            add.clear()


ans = 0
for n in mem:
    #print(n, mem[n])
    ans += int(mem[n])
print(ans)