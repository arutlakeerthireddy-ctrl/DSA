#what is subarray?
'''A subarray is a continuous part of an array
A subarray consists of consecutive(continuous) elements from the original array '''

#formula
'''
if array size is n
total no. of subarrays:n*(n+1)/2'''
#example:
'''
arr=[1,2,3,4]
n=4
total:4*5/2=10'''

#Types of subarrays
#1.Fixed-length subarray
'''
len=3
arr=[1,2,3,4,5]
subarrays:
[1,2,3]
[2,3,4]
[3,4,5]
used in sliding window'''
#2.variable-length subarray:length is not fixed
#ex:[1],[1,2],[1,2,3],[2],[2,3] used in prefix sum and two pointers

#How to print all subarrays
arr=[1,2,3]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        print(arr[i:j+1])
[1]
[1, 2]
[1, 2, 3]
[2]
[2, 3]
[3]

#Time complexity
'''
printing all subarrays:O(n**3)
-outer loop:O(n)
-inner loop:O(n)
-printing subarray:O(n)'''

#only counting subarrays:n*(n+1)/2-time complexity=O(1)

#Real world applications
'''
music playlist:songs played continuously from song 3 to song7
video streaming:watching a continuous part of a movie
stock market,weather analysis,banking,sports'''




