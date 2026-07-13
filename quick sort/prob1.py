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
arr=[8,9,2,1,4,8]
quicksort(arr,0,len(arr)-1)
print(arr)
print(count)
#output
[1, 2, 4, 8, 8, 9]
5

#or
#using lomuto partition
count=0
def lomuto(arr,low,high):
    global count
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            if i!=j:
                arr[i],arr[j]=arr[j],arr[i]
                count+=1
    if i+1!=high:
        arr[i+1],arr[high]=arr[high],arr[i+1]
        count+=1
    return i+1
def quicksort(arr,low,high):
    if low<high:
        pi=lomuto(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    
arr=[8,9,2,1,4,8]
quicksort(arr,0,len(arr)-1)
print(arr)
print(count)
#output
[1, 2, 4, 8, 8, 9]
8
