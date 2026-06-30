#Binary search:it is a searching algorithm used to find target value in sorted array or list by repeatedly dividing search space into two halves until target is found or search space becomes empty
#working:
'''
 1.consider sorted array
2.target value to search for
3.find the middle ement by dividing the array
4.if middle value is equal to target value,then returns found
5.if middle value is less than target value,then search in right array
6.if middle value is greater than target value,then search in left array
7.repeat until target is found or search space become empty'''

#example 
'''
1.arr=[2,7,9,10,22,30] #sorted array
2.target=22
3.mid=len(arr)//2=6//2=3  #at 3 indext mid value is 10 
mid[3]=10
4.so 10 is less than 22 then search consider above 10 is [22,30]
5.again find mid for [22,30] is 1, at index 1 mid value is 30
mid[1]=30
6.30>22 so find left arr i.e [22],hence we found
7.return original index of that value 4 '''

#algorithm:
'''
1.An array with values to search through
2.target value to search for
3.loop through array until left index less than,or equal to,right index
4.if statement to compare mid is equals to target,then returns index if target found
5.elif statement to compare mid<target,then returns update left by increasing mid index by 1
6.else statement to update right index by decreasing mid index by 1
7.returns -1 after loop to indicate target not found
'''
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[2,4,7,8,9,11]
target=9
print(binary_search(arr,target))#4
def binary_search_1(arr_1,target_element):
    left=0
    right =len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==target_element:
            return mid
        elif arr[mid]<target_element:
            left = mid+1
        else:
            right = mid -1
    return - 1
arr=[4,7,9,10,32]
target_element=10
print(binary_search_1(arr,target_element))#3



