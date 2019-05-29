a=int(input())
d=0
b=[int(a) for a in input().split()]
for i in range(0,len(b)-1):
    d=d^b[i]^b[i+1]
print(d)
