a,b=map(int,input().split())
f=[]
for i in range(a):
    s=set(map(int,input().split()))
    f.append(s)
#print(*f)
c=s.intersection(*f)
print(*c)
