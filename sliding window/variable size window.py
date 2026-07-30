#variable size sliding window:in a variable-size sliding window,the window size changes according to a condition
#Algorithm
'''
left=0
for right in range(len(arr)):
    Include arr[right]
    while condition is not valid:
        remove arr[left]
        left+=1
    update answer
    '''
#Smallest Subarray with Sum ≥ Target
def Subarray_sum(arr,target):
    subarr_sum=arr[:]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if sum(arr[i:j+1])>=target:
                if len(subarr_sum)>len(arr[i:j+1]):
                    subarr_sum=arr[i:j+1]
    return subarr_sum
arr=[2,3,1,2,4,3]
target=7
print(Subarray_sum(arr,target))#[4, 3],time:O(n**3)

#Better brute force approach(O(n**2))
#instead of calculating sum() every time ,maintain running sum
def Subarray_sum(arr,target):
    subarr_sum=arr[:]
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum+=arr[j]
            if current_sum>=target:
                if len(subarr_sum)>len(arr[i:j+1]):
                    subarr_sum=arr[i:j+1]
    return subarr_sum
arr=[2,3,1,2,4,3]
target=7
print(Subarray_sum(arr,target))#[4, 3],time:O(n**2)

#variable sliding window solution(optimal-O(n))
def variable_size(arr,tar):
    left=0
    current_sum=0
    min_length=float('inf')
    answer=[]
    for right in range(len(arr)):
        current_sum+=arr[right]
        while current_sum>=tar:
            if right-left+1<min_length:
                min_length=right-left+1
                answer=arr[left:right+1]
            curren_sum-=arr[left]
            left+=1
    return answer
arr=[2,3,1,2,4,3]
tar=7
print(Subarray_sum(arr,tar))#[4,3],time:O(n),space:O(1)


            