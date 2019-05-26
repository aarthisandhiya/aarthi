n,m=map(str,input().split())
s=[]
o=''
if len(m)==len(n):
    print(n+m)
elif len(n)>len(m):
    k=list(n)
    for i in range(len(m)):
        s.append(k[i])
    print(s)
    d="".join(list(s))
    print(d+m)
