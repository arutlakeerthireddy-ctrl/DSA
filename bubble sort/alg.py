#what is bubble sort:
'''it is a comparison based sorting algorithm that sorts elements by repeatedly comparing neighbouring elements
if left element>right element
then swap them
it continues this process until the array becomes sorted'''

#example
#original array:
[8,1,4,0,9]
#after sorting:
[0,1,4,8,9]

#why is it called bubble sort?
'''imagine bubbles in water
smaller bubbles stay at the bottom
larger bubbles rise to the top
similarly,
*in every pass, the largest element "bubbles up" to the end of the array'''

#working
'''take [5,3,8,4,2]
pass1: compare 5 and 3
swap:[3,5,8,4,2]
compare 5 and 8
no swap:[3,5,8,4,2]
compare:8 and 4
swap:[3,5,4,8,2]
compare:8 and 2
swap:[3,5,4,2,8]
largest element 8 reached the end
pass2:compare 3 and 5
no swap:[3,5,4,2,8]
compare:5 and 4
swap:[3,4,5,2,8]
compare:5 and 2
swap:[3,4,2,5,8]
second largest 5 reached
pass3:compare 3 and 4
no swap
compare:4 and 2
swap:[3,2,4,5,8]
third largest reached
pass4:compare 3 and 2
swap:[2,3,4,5,8]
Array sorted '''

#program
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([5,3,8,4,2]))#[2, 3, 4, 5, 8]

#bubble sort with optimization
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
            
    return arr
print(bubble_sort([5,3,8,4,2]))#[2, 3, 4, 5, 8]

#time complexity
'''
best(optimized,already sorted)-O(n)
avg-O(n**2)
worst-O(n**2)'''
#space complexity:O(1)