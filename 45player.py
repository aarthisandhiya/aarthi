o,a=map(int,input().split())
s=int(o/2)
b=int(a**0.5)
if(s*2==o and b*b==a):
	print("yes")
else:
	print("no")
