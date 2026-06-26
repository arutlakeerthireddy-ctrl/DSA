'''Find First Occurrence
Return the first index where the target appears.'''
def first_occur(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
print(first_occur([2,2,3,4,2],2))#0

'''Find Last Occurrence
Return the last index where the target appears.'''
def last_occur(arr,target):
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==target:
            return i
print(last_occur([2,2,3,4,5],2))#1

    