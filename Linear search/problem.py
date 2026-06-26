''' Find Maximum Element
Find the largest number by scanning every element.'''
def max_element(arr):
    high=arr[0]
    for i in range(len(arr)):
        if arr[i]>high:
            high=arr[i]
    return high
li=[2,4,8,9,10]
print(max_element(li))#10