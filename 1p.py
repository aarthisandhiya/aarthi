a=input()
x=''
for i in range(len(a)-1,-1,-1):
	x=x+str(a[i])+''
print(x.strip())
