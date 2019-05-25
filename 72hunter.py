aa=input().split()
s=''
for i in range(0,len(aa)):
    if i==int(len(aa)-1):
        d=list(aa[i])
        for j in d:
            if j!='.':
                s=s+str(j)+''
        if i%2==0:
            print(s[::-1],end=" ")
        elif i%2==1:
            print(s,end=" ")
    elif i%2==0:
        print(aa[i][::-1],end=" ")
    elif  i%2==1:
        print(aa[i],end=" ")
