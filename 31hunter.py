a=int(input())
b=list(map(int,input().split()))
k=[]
for i in range(0,a-1):
  n,n1=b[:i+1],b[i+1:]
  prod1,prod2=1,1
  #print(n,n1)
  for i in n:
    prod1*=i
  for i in n1:
    prod2*=i
  if prod1>prod2:
    k.append(prod1)
  else:
    k.append(prod2)
#print(l)
print(max(k))
