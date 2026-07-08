#counting sort:it is non comparison based sorting algorithm that sort an arr by counting how many times a unique element appears.
# it then uses these counts to place each element in its correct sorted position
#algorithm
'''
find maximum element in the input array
create count array with size (maximum+1) and initialize with 0's
traverse the input array find the frequencies of each element in input array 
traverse the count array from left index to maximum element
for each index:
   -if count[i]>0
   -place i in output array count[i] times
output array is sorted

'''
#program..
def counting_sort(arr):
    max_value=max(arr)
    count=[0]*(max_value+1)
    for num in arr:
        count[num]+=1
    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1
    return arr
arr=list(map(int,input().split()))
print(counting_sort(arr))#[0, 1, 5, 7, 9]
