a=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(0,a-1):
  n,n1=b[:i+1],b[i+1:]
  pr1,pr2=1,1
  #print(n,n1)
  for i in n:
    pr1*=i
  for i in n1:
    pr2*=i
  if pr1>pr2:
    k.append(pr1)
  else:
    k.append(pr2)
print(l)
print(max(l))
