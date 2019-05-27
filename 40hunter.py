a=int(input())
summ=0
while a>0:
    s=a%10 
    summ=summ+s 
    a=a//10 
summ=str(summ)
t=summ[::-1]
if t==summ:
    print("YES")
else:
    print("NO")
