a=input()
b=len(a)//2
#print(b)
s=a[:b]
#print(s)
k=a[b+1:]
if s==k:
    print("YES")
else:
    print("NO")
    
