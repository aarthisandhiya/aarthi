a=int(input())
b=[int(a) for a in input().split()]
i=0
while i<len(b):
    if b.count(b[i])==1:
        print(b[i])
        break
    else:
        i=i+1 
        
