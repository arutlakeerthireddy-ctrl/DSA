def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
           arr[j+1]=arr[j]
           j-=1
        arr[j+1]=key
    return arr
arr=[50,21,60,11,45]
print(insertion_sort(arr))