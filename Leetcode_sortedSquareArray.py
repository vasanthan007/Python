# Time = O(n logn) Space = O(n)
#Sorted Squared Array
def sorted_squared(array):
        n = len(array)
        res = [0]*n
        for i in range (n):
                res[i] = array[i] ** 2
        res.sort()
        return (res)
    
val = input("Enter elements separated by space: ").split()
arr = [int(num_str) for num_str in val]
print(sorted_squared(arr))
