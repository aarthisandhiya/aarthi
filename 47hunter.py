a=input()
s=[]
for i in range(0,len(a)):
    if a[i]==" " and a[i+1]==" ":
        if a[i] not in s:
            s.append(a[i])
    else:
        s.append(a[i])
        
for i in range(0,len(s)):
    x=len(s)-1
    if i!=x:
        print(s[i],end="")
    else:
        print(s[i])
        
