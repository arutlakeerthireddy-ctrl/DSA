'''Count Even Sum Prefixes
Count how many prefix sums are even.'''
def count_even(arr):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    count=0
    for num in prefix:
        if num%2==0:
            count+=1
    return count
arr=[4,9,2,1,3]
print(count_even(arr))#2

#time complexity:O(n)
#space complexity:O(n)

def count_even(arr):
    prefix_sum=0
    count=0
    for num in arr:
        prefix_sum+=num
        if prefix_sum%2==0:
            count+=1
    return count
arr=[4,9,2,1,3]
print(count_even(arr))#2
#space complexity:O(1)