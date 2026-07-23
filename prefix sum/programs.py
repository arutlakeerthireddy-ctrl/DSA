'''Minimum Prefix Sum
Find the minimum prefix sum.'''
def min_prefix(arr):
    prefix_sum=0
    minimum=float('inf')
    for num in arr:
        prefix_sum+=num
        minimum=min(minimum,prefix_sum)
    return minimum
arr=[6,8,1,3,4]
print(min_prefix(arr))#6

'''Find Prefix Sum at Index K
Return the prefix sum up to index K.'''
def prefix_sum(arr,k):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    return prefix[k]
arr=[5,2,0,8,1]
k=3
print(prefix_sum(arr,k))#15

'''Sum Between Two Indices
Given many (L,R) queries, answer each in O(1).'''
def sum_indices(arr,L,R):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    if L==0:
        ans=prefix[R]
    else:
        ans=prefix[R]-prefix[L-1]
    return ans
arr=[1,2,3,4,5]
L=2
R=4
print(sum_indices(arr,L,R))#12
