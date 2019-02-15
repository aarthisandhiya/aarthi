c=input()
x=' '
y=' '
for i in range(0,len(c)):
	if i%2==0:
		x=x+str(c[i])
	else:
		y=y+str(c[i])
print(str(x.strip())+" "+str(y.strip()))
