'''Longest Subarray with Sum ≤ K
Input:arr = [1,2,1,0,1,1,0]
k = 4'''
def Longest_subarray(arr,k):
    left=0
    current_sum=0
    max_length=0
    answer=[]
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>k:
            current_sum-=arr[left]
            left+=1
        if right-left+1>max_length:
            max_length=right-left+1
            answer=arr[left:right+1]
           
    return answer
arr = [1,2,1,0,1,1,0]
k = 4
print(Longest_subarray(arr,k))#[1, 0, 1, 1, 0]


    
