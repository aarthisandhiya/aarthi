c=input().split()
b=input()
for i in range(0,len(c)):
    if c[i]==b:
        f=c.count(c[i])
        print(f)
        break
else:
    print(0)
    
