a,b=map(int,input().split())
c=[int(a) for a in input().split()]
while b in c:
    c.remove(b)
if not c:
    print("empty")
else:
    print(*c)
