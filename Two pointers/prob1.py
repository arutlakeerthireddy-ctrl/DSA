'''
1. Pair with Given Sum
Problem: Given a sorted array and a target X, determine whether there exists a pair whose sum is X.
Example:
Input:
arr = [1, 2, 3, 4, 6]
X = 6
Output:
Yes (2 + 4)'''
def pair_sum(arr,x):
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==x:
            return (arr[left],arr[right])
        elif current_sum<x:
            left+=1
        else:
            right-=1
    return "No"
arr=[1, 2, 3, 4, 6]
x=6
print(pair_sum(arr,x))#(2,4)



