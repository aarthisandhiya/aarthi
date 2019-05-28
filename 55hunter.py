a,b=map(int,input().split())
c=[int(a) for a in input().split()]
f=[]
g=[]
k=[]
for i in range(0,b):
    f.append(c[i])
for j in range(b,len(c)):
    g.append(c[j])
#print(g)        
k.append(g)
k.append(f)
x=k[0]
y=k[1]
for x in k[0]:
    print(x,end=" ")
for y in k[1]:
    print(y,end=" ")
