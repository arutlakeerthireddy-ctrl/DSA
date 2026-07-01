'''Find the First Occurrence
Input:
arr = [1,2,2,2,3,4]
target = 2
Output:
1 '''
def first_occurrence(arr,target):
    ans=-1
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            ans=mid
            right=mid-1
        elif arr[mid]<=target:
            left=mid+1
        else:
            right=mid-1
    return ans
arr=[1,2,2,2,3,4]
target=2
print(first_occurrence(arr,target))
        