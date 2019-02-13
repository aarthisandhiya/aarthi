u=int(input())
x=' '
for i in range(1,u+1):
	if u%i==0:
		x=x+str(i)+' '
print(x.strip())
