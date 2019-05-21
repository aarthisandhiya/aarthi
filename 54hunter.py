a=input()
s=[]
b=[int(a) for a in input().split()]
s.append(b[0])
for i in range(0,len(b)):
    if b[i]<s[-1]:
        s.append(b[i])
    else:
        s.append(s[-1])
s.remove(s[0])
for i in range(0,len(s)):
    print(s[i],end=" ")
