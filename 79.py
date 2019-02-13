y,z=map(int,input().split())
a=y*z
for i in range(0,a):
	if i*i==a:
		print("yes")
		break
else:
	print("no")
