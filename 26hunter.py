a=int(input())
c=0
b=[int(a) for a in input().split()]
g=b[::-1]
x=len(b)-1
for i in range(0,len(g)):
    if i!=x:
        print(str(g[i])+'->',end="")
    else:
        print(g[i])
