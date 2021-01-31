x=0
T,D=map(eval,open("vstup.txt"))
n=p=1
s=T,
for b in D:
 if b:
  while(n+x)%b:n+=p
  p*=b;w,v=s=min(s,(-T%b,b))
 x+=1
print(w*v,n)