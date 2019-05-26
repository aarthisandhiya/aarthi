a=int(input())
f=1
s=[]
b=[int(a) for a in input().split()]
for i in range(a):
    for j in range(a):
        if i!=j:
            f=f*b[j]
    s.append(f)
    f=1 
d=len(s)
for i in range(d):
    if i!=d-1:
        print(s[i],end=" ")
    else:
        print(s[i])
            
