a,b=map(int,input().split())
c=0
n=[int(a) for a in input().split()]
m=[int(b) for b in input().split()]
for i in range(0,len(m)):
    for j in range(0,len(n)):
        if m[i]==n[j]:
            c=c+1 
if c==len(m):
    print("YES")
else:
    print("NO")
