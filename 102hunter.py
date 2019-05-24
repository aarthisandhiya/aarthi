a=int(input())
s=0
while a>0:
    r=a%10
    s=s+r*r 
    a=a//10
print(s)
