a=input()
mini=0
for i in range(0,len(a)):
    s=a.count(a[i])
    if s>mini:
        mini=s 
        d=a[i]
print(d)

