#hoare partition quick sort:
'''Hoare partition is a partitioning technique invented by tony hoare
it is usually faster than lomuto parition because it performs fewer swaps'''
#Algorithm
'''
1.choose the first element as pivot
2.initialize two pointers
i=low-1
j=high+1
3.move i from left to right until element>=pivot is found
4.move j from right to left until element<=pivot is found
5.if i<j,swap arr[i] and arr[j]
6.repeat until i>=j
7.return j (not pivot index)
'''
#program
def Hoare(arr,low,high):
    pivot=arr[low] #choose first element as pivot
    i=low-1 #left pointer
    j=high+1 #right pointer
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
           return j #partition index
        arr[i],arr[j]=arr[j],arr[i] #swap
def quicksort(arr,low,high):
    if low<high:
        pi=Hoare(arr,low,high)
        quicksort(arr,low,pi)
        quicksort(arr,pi+1,high)
    return arr

arr=[8, 3, 1, 7, 0, 10, 2]
print(quicksort(arr,0,len(arr)-1))#[0, 1, 2, 3, 7, 8, 10]

#properties
'''
1.divide and conquer algorithm
2.pivot selection
3.two pointers
4.fewer swaps
5.partition index
6.pivot not guaranteed to be in final position
7.in-place algorithm
8.not stable
9.time complexity
*best case:O(nlogn)
*avg case:O(nlogn)
*worst case:O(n**2) when poor pivots are chosen repeatedly
10.space complexity
*recursion stack:O(logn) on avg
*worst case:O(n) recursion depth
11.recursive calls:since hoare partition returns j ,recursive calls are:
quicksort(arr,low,j)
quicksort(arr,j+1,high)

'''
