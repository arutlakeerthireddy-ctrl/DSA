'''Find First Element Greater Than X
Input:
arr = [2,4,6,8,10]
x = 5
Output:
6 '''
def first_element(arr,x):
    left=0
    right=len(arr)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>x:
            ans=arr[mid]
            right=mid-1
        else:
            left=mid+1
            
    return ans
arr=[2,4,6,8,10]
x=5
print(first_element(arr,x))#6
        
    
'''Find Last Element Smaller Than X
Input:
arr = [2,4,6,8,10]
x = 7
Output:
6'''
def last_element(arr,x):
    left=0
    right=len(arr)-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<x:
            ans=arr[mid]
            left=mid+1
        else:
            right=mid-1
    return ans
arr = [2,4,6,8,10]
x = 7
print(last_element(arr,x))

