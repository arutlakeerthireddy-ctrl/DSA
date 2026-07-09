''' Check if Array is Already Sorted
Use counting sort logic to determine whether the array is already sorted.
Input:[1,2,3,4]
Output:Already Sorted '''
def counting_sort(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        count[num]+=1
    
    output=[]
    for i in range(len(count)):
        while count[i]>0:
            output.append(i)
            count[i]-=1
    if arr==output:
        return "Already sorted"
    else:
        return "Not sorted"
print(counting_sort([1,2,3,4]))# "Already sorted"
    

