a=input()
c=0
for i in range (0,len(a)):
	if a[i]=='1' or a[i]=='0':
		c=c+1
	else:
		break
if c==len(a):
	print("yes")
else:
	print("no")
