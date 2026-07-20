'''2. Count Pairs with Given Sum
Problem: Given a sorted array and a target, count the number of pairs whose sum equals the target.
Example:
Input:
arr = [1, 2, 3, 4, 5]
X = 6
Output:(1,5), (2,4)'''
def count_pairs_sum(arr,x):
    left=0
    right=len(arr)-1
    count=0
    while left<right:
        s=arr[left]+arr[right]
        if s==x:
            count+=1
            left+=1
            right-=1
        elif s<x:
            left+=1
        else:
            right-=1
    return count
arr=[1,2,3,4,5]
x=6
print(count_pairs_sum(arr,x))#2