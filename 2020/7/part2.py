import time
start = time.time()
with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n")]

def finder(color):
    counter = 0
    bagLine = findLine(color)
    if bagLine.find("no other bags") != -1:
        return 0
    else:
        for i in range(len(bagLine)):
            if bagLine[i].isnumeric():
                num = int(bagLine[i])
                counter += num + num*finder(bagLine[i+2:bagLine.find("bag", i)-1])
        return counter        
                
def findLine(color):
    for line in listA:
        if line.find(color, 0, line.find("contain")) != -1:
            return line

print(finder("shiny gold"))
print(time.time()-start)