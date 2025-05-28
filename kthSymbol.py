def kth_symbol(n, k):
    #if the n value is n it should return 0
    if(n==1):return 0
    #the value will grow 2 times the n value so we are taking the mid point
    length = 2 ** (n - 1)
    mid = length // 2
    #if the k value inside the mid value.
    if(k <= mid):
        return kth_symbol(n-1, k)
    #if the k value higher than mid we need to subtract the mid value
    else:
        return int(not (kth_symbol(n-1, k-mid)))

print("Enter the value N and K")
n=input(int())
k=input(int())

print(kth_symbol(int(n),int(k)))
