m,n=map(int,input().split())
a=[int(m) for  m in input().split()]
b=[int(n) for  n in input().split()]
r=[]
for j in range(0,len(b)):
    if b[j] in a:
        print(max(a),end=" ")
    else:
        a.append(b[j])
        print(max(a),end=" ")
       
