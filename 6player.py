a,b=map(str,input().split())
dict={}
kit=0
for i in range(0,len(a)):
    s=a[i]
    #print(s)
    j=i
    k=b[j]
    #print(k)
    dict.update({s:k})
    
#print(dict)
for i in a:
    for f in b:
        for k,j in dict.items():
            if k==i and j==f:
                kit=0
            else:
                kit=kit+1

if kit==0:
    print("yes")
else:
    print("no")

