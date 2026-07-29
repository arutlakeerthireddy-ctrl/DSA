'''Count Distinct Elements in Every Window
Input:arr = [1,2,1,3,4,2,3],k = 4
Output:3 4 4 3'''
def Count_Distinct(arr,k):
    result=[]
    freq={}
    for num in arr[:k]:
        freq[num]=freq.get(num,0)+1
    result.append(len(freq))
    for i in range(k,len(arr)):
        outgoing=arr[i-k]
        freq[outgoing]-=1
        if freq[outgoing]==0:
            del freq[outgoing]
        incoming=arr[i]
        freq[incoming]=freq.get(incoming,0)+1
        result.append(len(freq))
    return result
arr=[1,2,1,3,4,2,3]
k = 4
print(Count_Distinct(arr,k))#[3, 4, 4, 3]






