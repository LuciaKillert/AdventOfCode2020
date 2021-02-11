import time
start = time.time()
with open("vstup.txt", "r") as f:
    L = [x for x in f.read().split("\n\n")]

RuleBlock = L[0].split("\n")
rules = [] #tuples
ans= []

for rule in RuleBlock:
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



tickets = L[2].split("\n")
tickets = tickets[1:]
for t in tickets:
    ticket = [int(x) for x in t.split(",")]
    for num in ticket:
        counter = 0
        for rule in rules:
            if num >= rule[0] and num <= rule[1]:
                counter = 1
                break
        if counter == 0:
            ans.append(num)
#print(ans)
print(sum(ans))
print(time.time()-start)

tf = [1,2,3,4,5]

for tff in tf:
    if tff == 3:
        tf.remove(tff)
    print(tf)