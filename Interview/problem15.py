#Binary Search 
#Implement binary search to find a target value in a sorted array.
def Binary_search(arr,tar):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            left+=1
        else:
            right-=1
arr=[3,4,5,6,9]
print(Binary_search(arr,6))#3