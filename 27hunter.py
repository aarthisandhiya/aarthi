a=input()
c=0
g=a[::-1]
s=[]
x=len(g)-1
if a==g:
    for i in range(len(a)):
        if i!=x:
            s.append(a[i])
    for j in range(0,len(s)):
        y=len(s)-1
        if j!=y:
            print(s[j],end="")
        else:
            print(s[j])
elif a!=g:
    print(a)
