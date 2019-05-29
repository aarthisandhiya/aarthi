a=input()
s=''
for i in range(0,len(a)):
    if a[i].isupper():
        s=s+a[i].lower()+''
    else:
        s=s+a[i].upper()+''
print(s.strip())
        
    
