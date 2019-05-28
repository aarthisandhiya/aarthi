a,b=map(str,input().split())
s=len(a)
k=len(b)
g=[]
g.append(s)
g.append(k)
e=min(g)
print(e)
c=1
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            if a.count(a[i])==b.count(b[j]):
                c=c+1 
                #print(c)
                break
if c>=e:
    print("true")
else:
    print("false")
        
            
