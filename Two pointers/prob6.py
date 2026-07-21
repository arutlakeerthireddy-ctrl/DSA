'''Triplet with Given Sum
Problem: Given an array and a target, determine whether any three elements sum to the target.
Example:
Input:
arr = [1,4,45,6,10,8]
Target = 22
Output:
Yes
(4,8,10)'''
def Triplet_sum(arr,x):
    arr=sorted(arr)
    n=len(arr)
    triplet=()
    for i in range(n-2):
        left=i+1
        right=n-1
        while left<right:
            total=arr[i]+arr[left]+arr[right]
            if total==x:
                triplet=(arr[i],arr[left],arr[right])
                return triplet
            elif total<x:
                left+=1
            else:
                right-=1
    return triplet
    
arr=[1,4,45,6,10,8]
x=22
print(Triplet_sum(arr,x))#(4, 8, 10)

