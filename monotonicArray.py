def monotonic_array(array):
    #write code here
    n = len(array)
    if n == 0: return True
    first = array[0]
    last = array[n-1]
    
    
    if(first > last):
        for k in range(n-1):
            if(array[k] < array[k + 1]): return False
    elif first == last:
        for k in range(n-1):
            if(array[k] != array[k + 1]): return False
    else:
        for k in range(n-1):
            if(array[k] > array[k + 1]): return False
    return True
        
val = input("Enter elememts separated by space: ").split()
arr = [int(num_str) for num_str in val]
print(monotonic_array(arr))