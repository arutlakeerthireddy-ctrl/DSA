#Count swaps.
def count_swaps(arr):
    n=len(arr)
    count=0
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    return count
print(count_swaps([4,5,1,6,9,0]))#7

#Count comparisons.
def count_comparisons(arr):
    n=len(arr)
    count=0
    for i in range(n-1):
        for j in range(n-1-i):
            count+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return count
print(count_comparisons([4,5,1,6,9,0]))#15

#Print array after each pass.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(f"After pass {i+1}:",arr)
    
bubble_sort([4,5,1,6,9,0])
#output
'''
After pass 1: [4, 1, 5, 6, 0, 9]
After pass 2: [1, 4, 5, 0, 6, 9]
After pass 3: [1, 4, 0, 5, 6, 9]
After pass 4: [1, 0, 4, 5, 6, 9]
After pass 5: [0, 1, 4, 5, 6, 9]'''