n = int(input(""))
j = 1
for i in range(n):
    st = ""
    for x in range(0,j):
        st+="1 "
    print(st.strip())
    j+=2
