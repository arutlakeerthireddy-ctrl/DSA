#what is merge sort?
'''merge sort is a sorting algorithm that works in three steps
*divide the array into two halves
*sort each half recursively
*merge the two sorted halves into one sorted array'''

#program
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[8,3,4,5,9,2,1]
print(merge_sort(arr))#[1, 2, 3, 4, 5, 8, 9]

#time complexity:
'''Best=avg=worst=O(n log n)'''
#space:O(n)
#stable,not in-place
