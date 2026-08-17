'''
2.Discounted Sum
Given an array of integers and an integer n, find the sum of the n largest unique elements,
then subtract the largest of those n elements (a discount).Return the result. 
If n is greater than the number of unique elements, return 0.
INPUT / OUTPUT Input: arr (list), n (count). Output: discounted sum. 
Constraint: 1 ≤ n ≤ len(arr).
EXAMPLE Input: arr=[5,2,9,1,7,4,6], n=3 Output: 13   (9+7+6=22, minus 9)
Input: arr=[5,2,9,1,7,4,6], n=1 Output: 0    (9 minus 9)'''
def Discounted_sum(arr,n):
    arr1=sorted(set(arr))
    arr1.reverse()
    result=0
    if n>len(arr1):
        return 0
    result+=sum(arr1[:n])
    result=result-arr1[0]
    
    return result
arr=[5,2,9,1,7,4,6]
n=3
print(Discounted_sum(arr,n))#13



