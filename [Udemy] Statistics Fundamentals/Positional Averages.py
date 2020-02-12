#Positional averages

def median(values):
	values = quick_sort(values)
	if (len(values)%2) == 0:
		index = int(len(values)/2)
		result = (values[index] + values[index-1])/2
		return(result)
	else:
		index = (int(len(values)/2))
		return(values[index])
	
def mode(oneD):
	copy = oneD
	for i in oneD:
		copy.append(i)
		
	return(None)
	
#Supporting methods
	
def quick_sort(values):
	if values:
		pivot = values[0]
		smaller = [i for i in values[1:] if i < pivot]
		greater = [i for i in values[1:] if i >= pivot]
		return quick_sort(smaller) + [pivot] + quick_sort(greater)
	else:
		return(values)
	
mine = [10, 20, 11, 53, 67, 80]
print(quick_sort(mine))