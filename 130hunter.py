s=int(input())
m=0
for i in range(3,s):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i%10==3:
            m=m+i 
print(m)
        
        
