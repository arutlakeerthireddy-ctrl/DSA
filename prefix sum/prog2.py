'''
Maximum Prefix Sum
Find the maximum prefix sum in an array.
Example:
Input:[2,-1,5,-3]
Output:6'''
def max_prefix(arr):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    return max(prefix)
arr=[7,9,5,8,1]
print(max_prefix(arr))#30

def max_prefix(arr):
    prefix_sum=0
    maximum=0
    for num in arr:
        prefix_sum+=num
        maximum=max(maximum,prefix_sum)
    return maximum
arr=[7,9,5,8,1]
print(max_prefix(arr))#30