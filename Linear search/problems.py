'''Find an Element
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
print(find_element(myarr,target))#True

'''Count Occurrences
Count how many times a target appears.
Example:
Input: [2,3,2,4,2], target=2
Output: 3'''
def count_occurences(arr,target):
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
    return count
li=[2,3,2,4,2]
tar=2
print(count_occurences(li,tar))#3