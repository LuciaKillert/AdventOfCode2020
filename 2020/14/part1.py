with open("vstup.txt", "r") as f:
    L = [x for x in f.read().splitlines()]

mask = ''
mem = {}
add = 0
value = ''
for line in L:
    if line.startswith("mask"):
        mask = line[7:]
        #print(mask)
    else:
        add = line[4:line.index(']')]
        value = bin(int(line[line.index('=')+2:]))[2:]
        value = list('0'*(36-len(value)) + value)
        #print(''.join(value))
        for i in range(36):
            if mask[i] == '0':
                value[i] = '0'
            elif mask[i] == '1':
                value[i] = '1'
        #print(value)
        mem[add] = ''.join(value)

ans = 0
for n in mem:
    ans += int(mem[n],2)
print(ans)
