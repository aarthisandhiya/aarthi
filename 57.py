a,b=map(int,input().split())
f=0
c=[int(i) for i in input().split()]
for r in range(0,a):
	if c[r]==b:
		f=f+1
print(f)
