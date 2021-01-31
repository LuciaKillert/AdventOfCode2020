with open("vstup.txt", "r") as f:
    T = int(f.readline())
    L = [int(x) for x in f.readline().split(",") if x != 'x']

ans = [T, 0]
for num in L:
    temp = (T//num) + 1
    if (temp * num) - T < ans[0]:
        ans[0] = (temp * num) - T
        ans[1] = num
print(ans[0]*ans[1])