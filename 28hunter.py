a=input()
s=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if a[i]!=a[j]:
            if a[i] not in s:
                s.append(a[i])
for i in range(0,len(s)):
    x=len(s)-1
    if i!=x:
        print(s[i],end="")
    else:
        print(s[i])
