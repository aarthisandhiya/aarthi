my1=raw_input()
my = my1.split(" ")

s = int(my[0])
y = int(my[1])
c = int(my[2])

if s>y and s>c:
	print(s)
elif y>s and y>c:
	print(y)
else:
	print(c)
