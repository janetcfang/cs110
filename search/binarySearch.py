def search(list, item):
	min = 0
	max = len(list)-1
	found = False
	
	while min <= max and not found:
		midpoint = (min + max)//2
		if list[midpoint] == item:
			found = True
		else: 
			if item < list[midpoint]:
				max = midpoint - 1
			else:
				min = midpoint + 1
				
	return found
	
#main	
list = [3,32,61,4,99,45,32,93,111,7]
result = search(list,99)
print result
result = search(list,8)
print result
