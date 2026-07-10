#stable counting sort:it is a version of counting sort keeps the same order of duplicate elements how they appeared before and after sorting
# #algorithm
'''
Find the maximum element.
Create a count array.
Count the frequency of each element.
Convert the count array into a cumulative (prefix sum) array.
Create an output array.
Traverse the original array from right to left.
Place each element in its correct position using the count array.
Decrease the corresponding count.
Copy the output array back to the original array if needed.'''

#1.program 
def stable_counting_sort(arr): #arr=[4,7,8,1,3,4]
    max_value=max(arr) #8           0 1 2 3 4 5 6 7 8
    count=[0]*(max_value+1) #count=[0 0 0 0 0 0 0 0 0]
    for num in arr: #4                    0 1 2 3 4 5 6 7 8
        count[num]+=1 #count[4]=1  count=[0,1,0,1,2,0,0,1,1]
    for i in range(1,len(count)): #i=1 #2
        count[i]+=count[i-1] #count[1]=count[1]+count[0]=1 #count[2]=1 #count=[0,1,1,2,4,4,4,5,6]
    output=[0]*len(arr) #output=[0 0 0 0 0 0 ]
    for num in reversed(arr): #4
        output[count[num]-1]=num
        count[num]-=1
    return output
arr=[4,7,8,1,3,4]
print(stable_counting_sort(arr))#[1, 3, 4, 4, 7, 8]
