a=int(input())
s=0
f=int(len(str(a)))
while a>0:
    r=a%10
    s=s+r**f
    a=a//10 
print(s)
