x =input()
b=[]
for i in range(0,len(x)):
    if x.count(x[i])==1:
        b.append(x[i])
for j in range(0,len(b)):
    print(b[j],end="")
            
            
