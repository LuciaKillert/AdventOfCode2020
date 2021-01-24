with open("vstup.txt", "r") as f:
    L = [x for x in f.read().splitlines()]

y = 1
x = -10
R = 0
ys = 0
xs = 0

for line in L:
    if line[0] == 'R' or line[0] == 'L':
        if line[0] == 'R':
            R = int(line[1:])
        elif line[0] == 'L':
            R = 360 - int(line[1:])
        if R == 90:
            y, x = x, -y
        elif R == 180:
            y = -y
            x = -x
        elif R == 270:
            y, x = -x, y
    elif line[0] == 'N':
        y += int(line[1:])
    elif line[0] == 'S':
        y -= int(line[1:])
    elif line[0] == 'E':
        x -= int(line[1:])
    elif line[0] == 'W':
        x += int(line[1:])
    elif line[0] == 'F':
            ys += y * int(line[1:])
            xs += x* int(line[1:])
print(abs(xs) + abs(ys))
