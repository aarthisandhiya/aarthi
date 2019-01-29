w=int(input())
e=[int(i) for i in input().split()]
s=sorted(e)
for i in range(0,len(e)):
	print(s[i],end=" ")
