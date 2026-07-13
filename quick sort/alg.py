#quick sort:quick sort is a divide and conquer sorting algorithm
#it works by selecting a pivot element from the array, arrange the elements in the array which are smaller than pivot are placed left side of pivot element 
#the larger elemnts than the pivot are placed right side of pivot
#this process continues recursively untill array is sorted

#why we should learn quick sort
'''it is important sorting algorithm used in coding interviews
used in product based company interviews:google,microsoft,amazon,adobe,oracle
quick sort is faster than remaining algorithms'''

#real world applications
'''quick sort is used whenever huge amounts of data must be sorted quickly'''
#database systems:sorts employees by salary
#E-commerce websites:amazon sorts products by price,rating,popularity
#banking systems:sort transactions
#student management:sort students by marks,roll number,cgpa

#algorithm
'''
1.choose the pivot element from array
2.partition the array so that:
-all elements smaller than the pivot are placed left
-all elements greater than pivot are placed right
3.place the pivot in its correct position
4.recursively apply the same process to left subarray
5.recursively apply the same process to right subarray
6.continue until each subarray contains 0 or 1 element
7.the array is now completely sorted'''

#program:last element as pivot(lomuto partition scheme)
def partition(arr,low,high):#[8 3 1 7 0 10 2],0,6
    pivot=arr[high] #arr[6]=2
    i=low-1 #i=0-1=-1
    for j in range(low,high):#j=0,1,2,3,4,5
        if arr[j]<=pivot: #8<2-false,3<2,1<2-True,7<2-false,0<2,10<=2
            i+=1 #i=0,1,
            arr[i],arr[j]=arr[j],arr[i] #8,1=1,8-[1,3,8,7,0,10,2],3,0=0,3-[1,0,8,7,3,10,2]
    arr[i+1],arr[high]=arr[high],arr[i+1]#8,2=2,8-[1,0,2,7,3,10,8]
    return i+1 #2
def quick_sort(arr,low,high):
    if low<high:
        pivot_index=partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)
arr=list(map(int,input("Enter elements: ").split()))
quick_sort(arr,0,len(arr)-1)
print(arr)
'''
Enter elements: 8 3 1 7 0 10 2
[0, 1, 2, 3, 7, 8, 10]
'''









