a,k=map(str,input().split())
k=int(k)
s=""
for i in range(0,len(a)):
    if (i+1)%k==0:
        s=s+str(a[i].upper())+""
    else:
        s=s+str(a[i])+""
print(s.strip())
        
