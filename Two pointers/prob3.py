'''Move All Zeroes to the End
Problem: Move all zeroes to the end while maintaining the relative order of non-zero elements.
Example:
Input:[0,1,0,3,12]
Output:[1,3,12,0,0]'''
def move_zeroes(arr):
    if not arr:
        return 0
    slow=0
    for fast in range(len(arr)):
        if arr[fast]!=0:
            arr[slow],arr[fast]=arr[fast],arr[slow]
            slow+=1
    return arr
arr=[0,1,0,3,12]
length=move_zeroes(arr)
print(length)#[1, 3, 12, 0, 0]


