b=input()
s=' '
for i in range(0,len(b)):
	if i==0:
		s=s+b[i].upper()
	elif b[i]==' ':
		s=s+' '+b[i+1].upper()
	else:
		s=s+b[i]
print(s)
			
