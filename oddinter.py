q,w=map(int,input().split())
e=' '
for i in range(q+1,w):
	if i%2==1:
		e=e+str(i)+' '
print(e.strip())
