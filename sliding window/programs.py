'''Maximum Sum Subarray of Size K
Given an array and an integer k, find the maximum sum of any contiguous subarray of size k.
Example
Input: arr = [2,1,5,1,3,2], k = 3
Output: 9'''
def max_sum(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum
arr=[2,1,5,1,3,2]
k = 3
print(max_sum(arr,k))#9

'''Maximum Average Subarray
Find the maximum average value of any contiguous subarray of length k.
Example
Input: arr = [1,12,-5,-6,50,3], k = 4
Output: 12.75'''
def max_avg(arr,k):
    window_sum=sum(arr[:k])
    max_avg=window_sum/k
    for i in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_avg=max(max_avg,window_sum/k)
    return max_avg
arr=[1,12,-5,-6,50,3]
k=4
print(max_avg(arr,k))#12.75
