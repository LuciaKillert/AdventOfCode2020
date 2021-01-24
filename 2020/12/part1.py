with open("vstup.txt", "r") as f:
    L = [x for x in f.read().splitlines()]

y = 0
x = 0
R = 0

for line in L:
    R %= 360
    if line[0] == 'R':
        R += int(line[1:])
    elif line[0] == 'L':
        R -= int(line[1:])
    elif line[0] == 'N' or (line[0] == 'F' and R == 180):
        y += int(line[1:])
    elif line[0] == 'S' or (line[0] == 'F' and R == 90):
        y -= int(line[1:])
    elif line[0] == 'E' or (line[0] == 'F' and R == 0):
        x -= int(line[1:])
    elif line[0] == 'W' or (line[0] == 'F' and R == 270):
        x += int(line[1:])

print(abs(x) + abs(y))
