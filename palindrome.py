a=int(input())
c=a
d=0
while a>0:
	b=a%10
	d=d*10+b
	a=a//10
if d==c:
	print("yes")
else:
	print("no")
	
