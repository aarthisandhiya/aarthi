a=int(input())
b=[int(i) for i in input().split()]
s=sorted(b)
for i in range(0,len(b)):
	m=len(s)//2
print(s[m])
