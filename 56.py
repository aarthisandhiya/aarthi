a=input()
c=0
d=0
for i in range(0,len(a)):
	if (a[i].isalpha()):
		c=c+1
	

	elif (a[i].isnumeric()):
		d=d+1
		
if c>0 and d>0:
	print("Yes")
else:
	print("No")
