a,b,c=map(int,input().split())
s=[]
s.append(a)
s.append(b)
s.append(c)
e=0
for i in range(0,len(s)):
    if s[i]!=0:
        w=int(((s[i]-2)*180)/s[i])
        e=e+w
if e<=180:
    print("yes")
else:
    print("no")
