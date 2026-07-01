#Check Whether an Element Exists
#Return True if the target exists in the sorted array, otherwise False.
def element_exist(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return False
print(element_exist([1,2,3,4,5],4))#True

#Count Comparisons
#Modify binary search to return how many comparisons were made before finding (or not finding) the element.
def count_comparisons(arr,target):
    count=0
    left=0
    right=len(arr)-1
    while left<=right:
        count+=1
        mid=(left+right)//2
        if arr[mid]==target:
            return count
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
       
    return count
    
print(count_comparisons([1,2,3,4,5],4))#2