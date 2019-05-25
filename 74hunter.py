a = input()
y = input()
length = 0
maxxi = 0
maxy = 0
for i in range((len(y)-1)):
	for j in range(i,len(y)):
		if y[i:j+1] in a:
			temp = y[i:j+1]
			if len(temp) >= int(length):
				length = len(y[i:j+1])
				maxxi = i
				maxy = j
answer = y[maxxi:maxy+1]
print(answer)
