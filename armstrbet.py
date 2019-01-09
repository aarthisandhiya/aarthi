y,z=map(int,input().split())
x=' '
for i in range(y+1,z):
	s=0
	e=i
	while e:
		s=s+(e%10)**3
		e=e//10
	if s==i:
		x=x+str(i)+' '
print(x.strip())		
		
