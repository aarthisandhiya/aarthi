a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
count=0
d=0
j=1 
for i in range (0,2):
    if a[i]==b[i]==c[i]:
        count=count+1 
for i in range (0,2):
    if a[i]==a[j] and b[i]==b[j] and c[i]==c[j]:
        d=d+1
            
        
        
if count>0 or d>0:
    print("yes")
else:
    print("no")
