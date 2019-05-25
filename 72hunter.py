aa=input().split()
for i in range(0,len(aa)):
    if i%2==0:
        print(aa[i][::-1],end=" ")
    elif  i%2==1:
        print(aa[i],end=" ")
