import re
with open("vstup.txt", "r") as f:
    listA = [x for x in f.read().split("\n\n")]
valid = 0
listB = []
letters = ['a', 'b', 'c', 'd', 'e', 'f']
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for person in listA:
    tempValid = 0
    if person.count(":") == 8 or (person.count(":") == 7 and person.find("cid") == -1):
        byr = person[person.find("byr")+4:]
        iyr = person[person.find("iyr")+4:]
        eyr = person[person.find("eyr")+4:]
        hgt = person[person.find("hgt")+4:]
        hcl = person[person.find("hcl")+4:]
        ecl = person[person.find("ecl")+4:]
        pid = person[person.find("pid")+4:]
        if byr[:4].isnumeric():
            if int(byr[:4])>1919 and int(byr[:4])<2003:
                tempValid +=1
        if iyr[:4].isnumeric():
            if int(iyr[:4])>2009 and int(iyr[:4])<2021:
                tempValid +=1
        if eyr[:4].isnumeric():
            if int(eyr[:4])>2019 and int(eyr[:4])<2031:
                tempValid +=1
        if hgt.find("cm") != -1 and hgt[hgt.find("cm")-3:hgt.find("cm")].isnumeric():
            if int(hgt[hgt.find("cm")-3:hgt.find("cm")]) > 149 and int(hgt[hgt.find("cm")-3:hgt.find("cm")]) < 194:
                tempValid +=1
        elif hgt.find("in") != -1 and hgt[hgt.find("in")-2:hgt.find("in")].isnumeric():
            if int(hgt[hgt.find("in")-2:hgt.find("in")]) > 58 and int(hgt[hgt.find("in")-2:hgt.find("in")]) < 77:
                tempValid +=1
        if hcl[0] == "#" and hcl[1:7].isalnum():
            for k in range(1,7):
                if hcl[k].isalpha():
                    if hcl[k].count(hcl[k]) != 1:
                        break
                if k == 6:
                    tempValid += 1
        if eyes.count(ecl[:3]) == 1:
            tempValid+=1
        if pid[:9].isnumeric():
            if len(pid) > 9:
                if not pid[9].isnumeric():
                    tempValid+=1
            else:
                tempValid+=1
    if tempValid == 7:
        print(person, "\n")
        valid+=1
print(valid)