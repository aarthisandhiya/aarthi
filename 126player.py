a,k=map(int,input().split())
s=[]
b=[int(a) for a in input().split()]
for i in range(0,len(b)):
    if b.count(b[i])!=k:
        if b[i] not in s:
            s.append(b[i])
            
k=sorted(s)
print(*k)
