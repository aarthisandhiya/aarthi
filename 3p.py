a=int(input())
b=0
while a>0:
    q=a%10
    b=b*10+q
    a=a//10
print(b)
