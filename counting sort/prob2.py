'''Smallest Missing Non-negative Integer
Input:[0,1,2,4,5]
Output:3'''
def smallest_missing_integer(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        count[num]+=1
    
    for i in range(0,len(count)):
        if count[i]==0:
            return i
            
    return len(count)
arr=list(map(int,input().split()))#[0,1,2,4,5] 
print(smallest_missing_integer(arr))#3

