def search (list,item):
	i=0
	while i<len(list):
		if list[i]==item:
			return i
		i=i+1
	return -1
	
#main
list = [3,32,61,4,99,45,32,93,111,7]
result = search(list,99)
print result
result = search(list,8)
print result
