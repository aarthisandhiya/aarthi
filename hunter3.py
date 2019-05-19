a=int(input())
c=[]
count=0
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if b[i]==i:
        c.append(i)
        count=count+1 
if count>0:
    for i in c:
        print(i,end=" ")
else:
    print("-1")
