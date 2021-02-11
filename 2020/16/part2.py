import time
from copy import deepcopy
start = time.time()
with open("vstup.txt", "r") as f:
    L = [x for x in f.read().split("\n\n")]

RuleBlock = L[0].split("\n")
rules = [] #tuples

test = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#test = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(len(test), len(test[18]))
ansLines = []
tickets = []

def getRules():
    for k, rule in enumerate(RuleBlock):
        for i in range(2): #2 per line
            if i == 0:
                pointer = rule.find(":") +2
                num1 = rule[pointer:rule.find('-')]
                num2 = rule[rule.find('-')+1:rule.find(' ', rule.find('-'))]
            else:
                pointer = rule.find(" or ") + 4
                num1 = rule[pointer:rule.find('-', pointer)]
                num2 = rule[rule.find('-', pointer)+1:]
            num1 = int(num1)
            num2 = int(num2)
            rules.append((num1,num2))
        if rule.find("departure") != -1:
            ansLines.append(k)

def removeBad():
    ggg = 0
    global tickets
    tickets = L[2].split("\n")
    tickets = tickets[1:]
    ticketss = deepcopy(tickets)
    #print("tickets",len(tickets))
    for t in tickets:
        ticket = [int(x) for x in t.split(",")]
        for num in ticket:
            counter = 0
            for rule in rules:
                if rule == (36,591) or rule == (613,957):
                    #print(rule, num)
                    ggg +=1
                if num >= rule[0] and num <= rule[1]:
                    counter = 1
                    #break
            if counter == 0:
                ticketss.remove(t)
    print(ggg)
    tickets = ticketss

def getAnswer():
    print(len(tickets))
    for t in tickets:
        ticket = [int(x) for x in t.split(",")]
        for j, num in enumerate(ticket):
            for m, rule in enumerate(rules):
                if num >= rule[0] and num <= rule[1]:
                    #print(m, m//2, j)
                    #print("NUM",num)
                    test[m//2][j] += 1

getRules()
#rules = rules[:6*2]
#print(rules)
removeBad()
#print(tickets)
getAnswer()

#print(test)
for v, t in enumerate(test):
    for b, h in enumerate(t):
        if h == len(tickets):
            #pass
            print(RuleBlock[v]," ====" ,b)
        if b == 5:
            pass
            #print(h)
    #print(max(t))
#print(ansLines)
print(time.time()-start)

G = [97,101,149,103,137,61,59,223,263,179,131,113,241,127,53,109,89,173,107,211]
print(G[4]*G[0]*G[16]*G[17]*G[7]*G[10])