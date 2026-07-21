'''Find Closest Pair to Target Sum
Problem: Given a sorted array and a target, find the pair whose sum is closest to the target.
Example:
Input:
arr = [1,3,4,7,10]
Target = 15
Output:(4,10)'''
def closest_pair(arr,x):
    left=0
    right=len(arr)-1
    min_diff=float('inf')
    best_pair=()
    while left<right:
        s=arr[left]+arr[right]
        diff=abs(target-s)
        if diff<min_diff:
            min_diff=diff
            best_pair=(arr[left],arr[right])
        if s<x:
            left+=1
        elif s>x:
            right-=1
        else:
            return best_pair
    return best_pair
arr= [1,3,4,7,10]
target=15
print(closest_pair(arr,target))#(4,10)
    