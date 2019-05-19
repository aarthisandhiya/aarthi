a,b=map(str,input().split())
c=0
d=0
for i in range(0,len(a)):
    for j in range(i,i+1):
        if a[i]==b[j]:
            c=c+1
            break
        
if c==len(a)-1:
    print("yes")
else:
    print("no")
