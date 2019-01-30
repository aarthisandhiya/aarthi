a,b=map(int,input().split())
c=[int(i) for i in input().split()]
for r in range(0,a):
	if c[r]==b:
		print("yes")
		break
else:
	print("no")
