a=input()
b=input()
count=0
s=[]
for i in range(len(b)):
    j=i+1
    if b[i]==a[j]:
        k=0
    count=count+1 
    s.append(b[i])
    #print(s)
    #print(count)
if count==len(b):
    for k in range(len(a)):
        if str(s[0])==str(a[k]):
            print(k)
            break
        
    else:
        print("-1")
            
        
    
