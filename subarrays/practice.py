#Print all subarrays.
arr=[1,2,3,4]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        print(arr[i:j+1])

#Count total subarrays.
arr=[1,2,3,4]
count=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        count+=1
print(count)#10

#Find the longest subarray.
arr=[1,2,3,4]
long_arr=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if len(long_arr)<len(arr[i:j+1]):
            long_arr=arr[i:j+1]
print(long_arr)#[1, 2, 3, 4]

#Find the shortest subarray.
arr=[1,2,3,4]
short_arr=arr
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if len(short_arr)>len(arr[i:j+1]):
            short_arr=arr[i:j+1]
print(short_arr)#[1]

#Find the sum of every subarray.
arr=[1,2,3,4]
sum_arr=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        sum_arr.append(sum(arr[i:j+1]))
print(sum_arr)#[1, 3, 6, 10, 2, 5, 9, 3, 7, 4]