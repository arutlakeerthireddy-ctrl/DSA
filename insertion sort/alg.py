#what is insertion sort?
'''
Insertion sot is a comparison based,stable,in-place sorting algorithm.
it sorts an array by taking one element at a time and inserting it into its correct position in the already sorted part of the array'''

#real world applications
'''
1.Arranging playing cards
2.contact lists
3.student marks
4.online leaderboards
'''
#Types of insertion sort
#straight insertion sort:
'''
-basic insertion sort
-uses linear search to find the correct position'''
#Binary insertion sort
'''
-uses binary search to find the insertion position
-reduces comparisons
-still requires shifting elements'''

#algorithm
'''
1.Assume the first element is sorted
2.pick the next element as the key
3.compare the key with previous elements
4.shift all larger elements one position to right
5.insert the key into its correct position
'''
#program
def Insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(Insertionsort([9,3,0,67,12]))#[0, 3, 9, 12, 67]

#Time complexity
'''
Best case:O(n)
avg case:O(n^2)
worst case:O(n^2)'''

#space complexity:O(1)

