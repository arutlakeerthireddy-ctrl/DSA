''' Number of Distinct Elements
Find the number of unique elements using counting sort.
Input
[1,2,2,3,4,4,4]
Output
4 '''
def counting_sort(arr):
    count=[0]*(max(arr)+1)#[0 0 0 0 0]
    for num in arr:     #   0 1 2 3 4
        count[num]+=1  #[0,1,2,1,3]
    result=0
    for i in range(len(count)):
        if count[i]>=1:
            result+=1
    return result
print(counting_sort([1,2,2,3,4,4,4]))#4