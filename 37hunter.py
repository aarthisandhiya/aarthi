l=list(input())
for i in range(len(n)):
    t=l.copy()
    t.pop(i)
    if "".join(t)=="".join(t[::-1]):
        print("YES")
        break
else:
    print("NO")
