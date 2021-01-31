import itertools
L = [29, 41, 661, 13, 17, 23, 521, 37, 19]
T = [19, 10, 13, 1, 9, 8, 6, 13]

def func():
    for a in itertools.count(661, 661):
        if a%29 == 0 and a%41 == 31 and a%13 == 0 and a%17 == 3 and a%23 == 0 and a%521 == 490 and a%37 == 0 and a%19 == 12:
            return a

#print(func())

def func2():
    for a in itertools.count(L[0], L[0]):
        if a%L[1] == L[1]-T[0] and a%L[2] == L[2]-sum(T[0:2]) and a%L[3] == L[3]-sum(T[0:3]) and a%L[4] == L[4]-sum(T[0:4]) and a%L[5] == L[5]-sum(T[0:5]) and a%L[6] == L[6]-sum(T[0:6]) and a%L[7] == L[7]-sum(T[0:7]) and a%L[8] == L[8]-sum(T[0:8]):
            return a

def func3():
    for a in itertools.count(213890632230818-320827, 320827):
        if a%320827 == 0 and a%41 == 31 and a%17 == 3 and a%521 == 490 and a%19 == 12:
            return a
        print(a)
            
print(func3())