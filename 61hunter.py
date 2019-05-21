a=int(input())
c=0
b=[int(a) for a in input().split()]
u,v=map(int,input().split())
for i in range(0,len(b)):
    if b[i]==u:
        while b[i]<int(v):
            c=c+1 
            i=i+1
print(c)
