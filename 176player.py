a,b=map(str,input().split())
c=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            if a.count(a[i])==b.count(b[j]):
                c=c+1 
                #print(c)
                break
if c>=len(a)-1:
    print("true")
else:
    print("false")
        
            
