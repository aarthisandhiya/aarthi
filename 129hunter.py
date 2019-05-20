s=int(input())
m=0
d=[int(s) for s in input().split()]
for i in range(0,len(d)):
    if d.count(d[i])>m:
        m=d.count(d[i])
        ssk=d[i]
print(ssk)
