def rightRotate(lists, num): 
	output_list = [] 
	for item in range(len(lists) - num, len(lists)): 
		output_list.append(lists[item])
	for item in range(0, len(lists) - num): 
		output_list.append(lists[item]) 
	for i in range(0,len(output_list)-1):
	       print(output_list[i],end=" ")
	else:
	    print(output_list[i+1])
	   
a,rotate_num=map(int,input().split())
list_1=[int(a) for a in input().split()]

if len(list_1)==1:
    print(*list_1)
else:
    rightRotate(list_1, rotate_num)
