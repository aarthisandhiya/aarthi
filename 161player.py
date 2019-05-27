a=int(input())
d=[]
num=0
count=0
for i in range(a):
    s=input()
    num=num+1 
    d.append(s)
#print(d)
for i in d:
    s=i 
    s=s.lower()
    #print(s)
    e=len(s)
    for j in range(0,e):
        if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
            count=count+1
if count>=num:
    print("yes")
else:
    if count==0:
        print("no")
            
