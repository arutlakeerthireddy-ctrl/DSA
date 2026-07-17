#Two pointers in python
#what is two pointers:
'''
Two pointers technique uses two variables(pointers) to traverse an array or string.instead of using nested loops,we move pointers based on certain conditions to solve problems effieciently
it  helps reduce time complexity from O(n**2) to O(n) in many problems
'''
#Why do we study two pointers?
'''
#Reduces time complexity
# uses less extra memory
# frequently asked in product based company interviews
# works well with sorted arrays and strings'''
#Types of two pointers
#1.opposite direction(left and right)
'''one pointer starts from the beginning and the other starts from the end
#example:
array=[1,2,3,4,6]
       L       R   '''
#pogram1: Find if there are two numbers whose sum is equal to the target.
def Two_pointers(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return True
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return False
arr=[1,2,3,4,5,7]
print(Two_pointers(arr,9))#True

#Time complexity:O(n)
#space complexity:O(1)

#2.Reverse an array
def Reverse_array(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=[1, 2, 3, 4, 5]
print(Reverse_array(arr))#[5, 4, 3, 2, 1]

#check palindrome
def check_palindrome(arr):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]!=arr[right]:
            return False
        left+=1
        right-=1
    return True
print(check_palindrome("madam"))
print(check_palindrome([1,2,1]))

        

    
