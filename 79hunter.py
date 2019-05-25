a=int(input())
b=[int(a) for a in input().split()]
if a%2==1:
    c=a//2
    print(b[c])
    b.remove(b[c])
    while len(b)>0:
        r=len(b)//2
        w=(b[r]+b[r-1])//2
        print(w)
        b.remove(b[r])
        b.remove(b[r-1])
    
elif a%2==0:
    d=a//2
    f=(b[d]+b[d-1])//2
    print(f)
    b.remove(b[d])
    b.remove(b[d-1])
    while len(b)>0:
        r=len(b)//2
        w=(b[r]+b[r-1])//2
        print(w)
        b.remove(b[r])
        b.remove(b[r-1])

        
        
    
    
