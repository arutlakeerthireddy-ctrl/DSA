'''Find Duplicate Numbers
Input:[1,2,2,3,4,4,5]
Output
2
4 '''
def counting_sort(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        count[num]+=1
    duplicates=[]
    for i in range(len(count)):
        if count[i]>1:
            duplicates.append(i)
    return duplicates
print(counting_sort([1,2,2,3,4,4,5]))#[2, 4]

    
    