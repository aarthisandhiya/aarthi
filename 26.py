q=int(input())
u=[int(i) for i in input().split()]
t=sorted(u)
for i in range(0,len(u)):
	print(t[i],' ',end="")
