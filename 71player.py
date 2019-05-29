a=int(input())
b=[int(a) for a in input().split()]
#print(b)
s=[]
for i in range(0,len(b)-1):
    j=i+1 
    if j>i:
        s.append(b[j])
    elif i>j:
        s.append(b[i])
print(*s)
    
