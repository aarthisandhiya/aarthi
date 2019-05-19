a=int(input())
c=[]
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if b[i]==i:
        c.append(i)
for i in c:
    print(i,end="")
