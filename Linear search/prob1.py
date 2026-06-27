'''Find Minimum Element
Find the smallest number.'''
def min_element(arr):
    minimum=arr[0]
    for i in range(len(arr)):
        if arr[i]<minimum:
            minimum=arr[i]
    return minimum
print(min_element([8,4,1,6]))

'''Find Sum of Elements
Calculate the total sum by visiting every element.'''
def sum_elements(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    return total
print(sum_elements([10,6,34,2]))#52

'''Count Even Numbers
Return the number of even integers in the array.'''
def count_even(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count+=1
    return count
print(count_even([4,5,8,10]))#3

'''Find Negative Numbers
Print all negative values.'''
def neg_num(arr):
    li=[]
    for i in range(len(arr)):
        if arr[i]<0:
            li.append(arr[i])
    return li
print(neg_num([-5,0,1,-1]))#[-5, -1]
