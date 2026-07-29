'''Count Even Numbers in Every Window
Input:arr = [2,3,4,6,7],k = 3
Output:2 2 2'''
def Count_even(arr,k):
    window=arr[:k]
    Count_even=[]
    count=0
    for num in arr[:k]:
        if num%2==0:
            count+=1
    Count_even.append(count)
    for i in range(k,len(arr)):
        if window[0]%2==0:
            count-=1
        window.pop(0)
        window.append(arr[i])
        if arr[i]%2==0:
            count+=1
        Count_even.append(count)
    return Count_even
arr=[2,3,4,6,7]
k = 3
print(Count_even(arr,k))#[2, 2, 2]
#Time:O(nk)
#space:O(k)

#without using window list and pop
def Count_even(arr,k):
    result=[]
    count=0
    for i in range(k):
        if arr[i]%2==0:
            count+=1
    result.append(count)
    for j in range(k,len(arr)):
        if arr[j-k]%2==0:
            count-=1
        if arr[j]%2==0:
            count+=1
        result.append(count)
    return result
arr=[2,3,4,6,7]
k = 3
print(Count_even(arr,k))#[2,2,2]
#Time complexity:O(n)
#space:O(1)

        