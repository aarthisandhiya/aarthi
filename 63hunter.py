a=int(input())
b=[int(a) for a in input().split()]
c=b[1:]
#print(len(c))
#print(c)
lst1=[]
print(max(c),end=" ")

for i in range(1,len(c)):
    minn=c[i]
    #print(minn)
    for j in range(i+1,len(c)):
        #print(minn,'=',c[j])
        if c[j]>minn:
            k=0
            minn=c[j]
        #print(minn)
    lst1.append(minn)
    
            

lst1.append(0)
for i in range(0,len(lst1)):
    if i!=len(lst1)-1:
        print(lst1[i],end=" ")
    else:
        print(lst1[i])

    
