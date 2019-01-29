m,n=map(int,input().split())
x=' '
for e in range(m+1,n):
	if e>0:
		for i in range(2,e):
			if e%i==0:
				break
		else:
			x=x+str(e)+' '
print(x.strip())			
	
		
