s=[]
a=int(input())
for i in range(2,a):
    for j in range(2,i):
        for k in range(2,a):
            for l in range(2,k):
                if i%j!=0 and k%l!=0 and i+j+k==a:
                    s.append(j)
                    s.append(i)
                    s.append(k)
                    break
print(s[0],s[1],s[2])
            
