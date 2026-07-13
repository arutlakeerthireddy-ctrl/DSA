#Count the number of swaps made during Quick Sort.
count=0
def Hoare(arr,low,high):
    global count
    pivot=arr[low]
    i=low-1
    j=high+1
    
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
        count+=1
    
def quicksort(arr,low,high):
    if low<high:
        pi=Hoare(arr,low,high)
        quicksort(arr,low,pi)
        quicksort(arr,pi+1,high)
    return count
    
arr=[8,9,2,1,4,8]
print(quicksort(arr,0,len(arr)-1))#5
#print(arr)
#print(count)
