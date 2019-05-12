a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
count=0
for i in range (0,2):
    if a[i]==b[i]==c[i]:
        count=count+1 
        break
        
        
if count>0:
    print("yes")
else:
    print("no")
