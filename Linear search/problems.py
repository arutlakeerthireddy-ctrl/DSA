'''1.Find an Element
Given an array and a target, return whether the target exists.
Example:
Input: [5, 3, 8, 2], target = 8
Output: True'''
def find_element(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return True
myarr=[5,3,8,2]
target=8
print(find_element(myarr,target))