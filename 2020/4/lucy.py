subor=open("vstup.txt","r")

x=subor.read()
abeceda=["a","b","c","d","e","f"]
lista=x.split("\n\n")
moznost=[]
moznost1=[]
chech=["byr","iyr","eyr","hgt","ecl","pid","hcl"]
counter=-1
count=0
eye=["amb","blu","brn","gry","grn","hzl","oth"]

for e in range (0,len(lista)):
    count=0
    index=0
    d=lista[e]
    for i in range(0,7):
        
        if lista[e].count(chech[i])==1:
            if i==0:
                hodnota=0
                index=lista[e].find(chech[i])+4
                hodnota=int(d[index:index+4])
                        
                if 1920<=hodnota<=2002:
                    count+=1
                   
            if i==1:
                hodnota=0
                index=lista[e].find(chech[i])+4
                hodnota=int(d[index:index+4])
                if 2010<=hodnota<=2020:
                    count+=1
                
            if i==2:
                hodnota=0
                index=lista[e].find(chech[i])+4
                hodnota=int(d[index:index+4])
                if 2020<=hodnota<=2030:
                    count+=1
                
            if i==3:
                hodnota=0
                check=lista[e].find("cm")
                
                if check>0:
                    index=check-3
                    if d[index].isnumeric()==True:
                        hodnota=int(d[index:index+3])
                        if 150<=hodnota<=193:
                            count+=1
                if check<0:
                    index=lista[e].find("in")-2
                    
                    if d[index].isnumeric()==True:
                        hodnota=int(d[index:index+2])
                        
                        if 59<=hodnota<=76:
                            count+=1
                
            if i==4:
                index=lista[e].find(chech[i])+4
                
                hodnota=d[index:index+3]
                
                pravda=False
                for h in range(0,7):
                    if eye[h]==hodnota:
                        pravda=True
                
                if pravda==True:
                    count+=1
                
            if i==5:
                if d.find(chech[i])>=0:
                    index=lista[e].find(chech[i])+4
                    moznost=d[index:]
                    
                    w=moznost.find(" ")
                
                    if len(moznost)==9:
                        count+=1
                    elif len(moznost)>9:
                        
                        if moznost[0:9].isdigit()==True and moznost[9].isdigit()!=True:
                            count+=1
                    
                       
            if i==6:
                hodnota=0
                index=lista[e].find(chech[i])+4
                countie=0
                if d[index]=="#":
                    for j in range(1,7):
                        ind=index+j
                        if abeceda.count(d[ind])>=1 or d[ind].isdigit()==True:
                            countie+=1
                    if countie==6:
                        count+=1          
    if count==7:
        counter+=1
    


    
print(counter)
subor.close()