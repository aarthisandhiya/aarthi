q=int(input())
key=0
i=1
while i<=q:
	if q%i==0:
		key=key+1
	i+=1
if key==2:
	print("yes")
else:
	print("no")
	
