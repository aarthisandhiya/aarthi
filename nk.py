b,c=map(int,input().split())
x=[int(i) for i in input().split()]
if b>=c:
	s=[]
	for i in range (0,c):
		s.append(x[i])
	print(sum(s))
