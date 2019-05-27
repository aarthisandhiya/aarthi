a=int(input())
k="kabali"
k=list(k)
lst1=[]
y=''
count=0
print(k)
for i in range(a):
    s=input()
    if len(s)==6:
        for i in range(0,len(s)):
            for j in range(0,len(k)):
                if k[j]==s[i]:
                    kit=0
            count=count+1
            y=y+str(s[i])+''
            y=''
        lst1.append(y)  
                    
print(lst1)       
#print(s)
