#Second Largest Number
#Write a function to find the second largest number in an array.
def Second_large_num(arr):
    arr1=sorted((set(arr)))
    arr1.reverse()
    return arr1[1]
arr=[4,6,8,1,9]
print(Second_large_num(arr))#8
