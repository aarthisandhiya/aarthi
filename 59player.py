a=int(input())
b=[int(a) for a in input()]
#print(b)
s=[]
for i in range(0,len(b)):
    if b[i]==0:
        #print(b[i])
        d=b[:i]
       # print(d)
        for k in d:
            if k!=0:
                kit=0
                s.append(k)
print(*s[0:6])
