#prefix sum
'''A prefix array stores cumulative sum of all elements from the beginning of the array to current index'''
#Formula:prefix[i]=arr[0]+arr[1]+...+arr[i]
#prefix[i]=prefix[i-1]+arr[i]

#example
#arr=[2,4,6,8,10]
#prefix_sum=[2,6,12,20,30]

#why do we study prefix sum?
'''without prefix sum ,if someone ask find the sum of elements from left to right
we have to calculate it again like 2+4+6+8=20
time=O(n)
it becomes very slow
prefix sum makes each query O(1)'''

#real life analogy
'''
Imagine your bank balance
every day you save money
day1=100
day2=200
day3=300
day4=400
running total becomes
100
300
600
1000
this running total is exactly a prefix sum'''

#syntax
arr=[1,2,3,4,5]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)#[1, 3, 6, 10, 15]

#algorithm
'''
1.create a prefix array
2.store the first element
prefix[0]=arr[0]
3.calculate cumulative sums
prefix[i]=prefix[i-1]+arr[i]
4.to find the sum from L to R
if L==0
sum=prefix[R]
otherwise
sum=prefix[R]-prefix[L-1]
'''
#example
arr=[3, 5, 2, 7, 4]
prefix=[3,8,10,17,21]
#find sum from index 1 to 3
#normal calculation=5+2+7=14
#using prefix sum:17-3=14

#Range sum query program
arr=[2, 4, 6, 8, 10]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

L=1
R=3
if L==0:
    ans=prefix[R]
else:
    ans=prefix[R]-prefix[L-1]
print(ans)#18

#Time complexity
'''
Building prefix sum:O(n)
one range query:O(1)
multiple queies:
-build:O(n)
-queries:O(q)
Total:O(n+q)'''
#space complexity:Extra prefix array:O(n)

#Types of prefix sum
#1.one-dimensional prefix sum:used for arrays
#2.Two-dimensional prefix sum:used for matrices,image processing,grid problems
#3.prefix XOR:prefix[i]=prefix[i-1]^arr[i]-used in bit manipulation
#4.prefix product:stores cumulative multiplication
#5.prefix frequency:stores cumulative frequency counts








