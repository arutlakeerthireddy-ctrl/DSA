#sliding window:A sliding window is an algorithmic technique where we maintain a window (continuous part) of an array or string  and move it step by step instead of checking every possible subarray
#instead of repeatedly processing same elements,we remove one element and add one new element while moving,this saves a lot of time.

#Example
'''
arr=[2,4,6,8,10]
window_size=3
#initially
[2,4,6] 8 10
#move one step
2 [4 6 8] 10
#move again
2 4 [6 8 10]'''

#why should we study sliding window
'''
without sliding window
suppose an array has 100000 elements
if we generate every subarray
the complexity becomes O(n**2)
which is very slow
*sliding window reduces many problems to O(n) '''

#example:Find maximum sum of 3 consecutive numbers.
'''
arr=[2,5,1,8,2]
calculate
2+5+1
5+1+8
1+8+2
each tie we should recalculate almost everything

#sliding window
current sum:2+5+1=8
move one step
remove 2,add 8
8-2+8=14
move again
remove 5,add 2
14-5+2=11
no repeated calculations
'''
#where is sliding window used in real life
'''
1.video streaming(youtube,netflix)
2.cpu monitoring
3.stock market
4.whether forecast'''

#when should i think of sliding window?
'''
whenever i see words like
*continuous
*consecutive
*subarray
*substring
*largest
*smallest
*maximum
*minimum
*fixed length
*longest
*shortest'''

#Types of sliding window
#1.fixed size sliding window:window size never changes
#2.variable size sliding window:
'''
window size changes
sometimes it increases
sometime it decreases
#ex:longest substring without repeating characters
if duplicate appears
shrink window
otherwise,expand window'''

#fixed window algorithm
'''
suppose window size=k
1.find first window sum
2.store answer
3.move window
4.subtract left element
5.add right element
6.update answer
7.repeat'''

#program:Find maximum sum of 3 consecutive numbers.
def max_sum(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i] #add new element
        window_sum-=arr[i-k] #remove old element
        max_sum=max(max_sum,window_sum)
    return max_sum
arr=[2,5,1,8,2,9,1]
print(max_sum(arr,3))#19

#rime complexity:O(n)
#space complexity:O(1)




