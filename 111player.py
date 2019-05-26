n,m=map(int,input().split())
d=[int(n) for n in input().split()]
s=d[0:n]
k=d[n:]
lst1=[]
for i in s:
    for j in k:
        if i==j:
            lst1.append(i)
            break
lst1=sorted(lst1)
for i in range(len(lst1)):
    x=len(lst1)-1
    if i!=x:
        print(lst1[i],end=" ")
    else:
        print(lst1[i])
