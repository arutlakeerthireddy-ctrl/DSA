''' Sort Only Even Numbers
Input:[5,4,3,2,1]
Output:[5,2,3,4,1]
'''
def even_sort(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        if num%2==0:
            count[num]+=1
    even=[]
    for i in range(len(count)):
        while count[i]>0:
            even.append(i)
            count[i]-=1
    k=0
    for j in range(len(arr)):
        if arr[j]%2==0:
            arr[j]=even[k]
            k+=1
        
    return arr
print(even_sort([5,4,3,2,1]))#[5, 2, 3, 4, 1]
        

