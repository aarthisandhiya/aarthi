n=int(input())
l=[int(x) for x in input().split()]
m=max(l)
a=0;b=0;f=0
for i in range(0,n-1):
  for j in range(i+1,n):
    if (l[i]+l[j])==0:
      print(l[i],l[j])
      f=1
      break
    else:
      if abs(l[i]+l[j])<m:
        m=abs(l[i]+l[j])
        a=i
        b=j

else:
    print(l[a],l[b])
