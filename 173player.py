a=input().split()
b=input().split()
c=list(a)
d=list(b)
s=[]
for i in a:
    if i not in b:
        s.append(i)
print(*s)
