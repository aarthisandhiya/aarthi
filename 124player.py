a=int(input())
c=0
s=[]
b=[int(a) for a in input().split()]
for i in range(1,1000):
    for j in range(0,len(b)):
        if i%b[j]==0:
            c=c+1
            continue
            #print(b[j])
        else:
            break
    if c==a:
        break
    c=0
print(i)
