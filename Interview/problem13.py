#Missing Number 
# Given an array of numbers from 1 to n with one missing, find the missing number.
arr=[1,2,3,5,6]
n=len(arr)
for i in range(1,n):
    if i not in arr:
       print(i)#4
       

    
        
    
