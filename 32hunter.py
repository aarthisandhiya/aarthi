def abc(klee):
    o=[]
    for i in range(0,len(klee)):
        if i%2==1:
            o.append(klee[i])
    #print(o)
    return o


a=int(input())
k=[int(a) for a in input().split()]
b=k
#o=[]
while (len(k)!=1):
    k=abc(k)
print(b.index(k[0]))


