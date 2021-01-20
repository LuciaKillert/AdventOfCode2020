import time

start = time.time()
subor=open("vstup.txt","r")

x=subor.read()
lista=x.split("\n")
res=[]

def mainFunc(item):
    results = 0
    line = lista[findLine(item)]
    temp = findNext(line)
    results += temp
    res.append(results)
    return temp


def findLine(item):
    for i in range(0, len(lista)):
        b = lista[i].find("bag")
        prvy = lista[i][:b-1]
        if prvy == item:
            return i

def findNext(line):
    tempResult = 0
    for i in range(0,len(line)):
        if line[i].isdigit():
            d = line[i+2:]
            b = d.find("bag")
            newItem = d[:b-1]
            t = mainFunc(newItem)
            tempResult += t*int(line[i]) + int(line[i])
    return tempResult
        
mainFunc("shiny gold")
print(res[len(res)-1])
print(time.time()-start)