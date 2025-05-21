def sorted_squared(array):
    #write code here.make sure to return desired array
    n = len(array)
    i,j = 0, n-1
    res = [0]*n
    for k in reversed(range(n)):
    	arr_i = array[i] ** 2
    	arr_j = array[j] ** 2
    	if(arr_i > arr_j):
    		res[k]  = arr_i
    		i += 1
    	else:
    		res[k] = arr_j
    		j -= 1
    return(res)
    
val = input("Enter elememts separated by space: ").split()
arr = [int(num_str) for num_str in val]
print(sorted_squared(arr))
    		
    
