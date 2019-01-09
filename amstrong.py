a=int(input())
e=a
s=0
while e>0:
	b=e%10
	s=s+(b*b*b)
	e=e//10
if a==s:
	print("yes")
else:
	print("no")
