a=input()
s=a[::-1]
for i in range(0,len(s)):
    if i==len(s)-1:
        break
    else:
        print(s[i],"-",end="")
print(s[-1])
