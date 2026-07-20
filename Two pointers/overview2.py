#2.same Direction(Fast and slow)
'''Both pointers move from left to right
array=[1,1,2,2,3]
       s f         '''

#ex:Remove Duplicates from Sorted Array
def remove_duplicates(arr):#[1,1,2,2,3]
    if not arr:
        return 0
    slow=0
    for fast in range(1,len(arr)):#fast=1,2,3,4
        if arr[slow]!=arr[fast]: #1==1 #1!=2 #2=2 #2=2
            slow+=1 #slow=1 #slow=2 
            arr[slow]=arr[fast] #arr[1]=arr[2] -[1,2,2,2,3]  #arr[2]=arr[4] -[1,2,3,2,3]
    return slow+1 #3
arr=[1,1,2,2,3]
length=remove_duplicates(arr)
print(length)
print(arr[:length])#3,[1, 2, 3]



