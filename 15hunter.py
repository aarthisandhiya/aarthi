a=int(input())
b=[int(a) for a in input().split()]
#print(b)
lis=[]
for i in range(len(b)-1,-1,-1):
    if b[i]<b[i-1]:
        if b[i] not in lis:
            lis.append(b[i])
        d=b[i-1:]
        #print(d)
        for k in range(1,len(d)):
            minn=d[0]
            if k<len(d):
                if d[k]<minn:
                    #print(d[k],"===")
                    kit=0
                    if minn not in lis:
                        lis.append(minn)
        #print(lis)
    #lis.append(b[i])
    else:
        break
lis=lis[::-1]
for i in range(0,len(lis)):
    if i!=len(lis)-1:
        print(lis[i],end=" ")
    else:
        print(lis[i])
s=max(lis)    
print(s)
