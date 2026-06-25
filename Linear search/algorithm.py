#Linear serach
'''1.consider the array with values to search through
2.A target value to search for
3.loop through array from start to end
4.An if statement is used to compare current value with target value,if they are equal it returns index of current value
5.After the loop returns -1,beacause at this point we know that the target value has not been found'''

#program
def Linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
li=[2,7,8,1,0]
x=8
#print(Linearsearch(li,x))#2
result=Linearsearch(li,x)
if result!=-1:
    print("Found at index:",result)#Found at index: 2
else:
    print("Not Found")

#Time complexity:O(n)
#note:single loop:O(n),Nested loops:O(n*2),triple loops:O(n*3),loop dividing by 2:O(logn)
'''Easy Memory Trick 🎯
O(1)      → Excellent
O(log n)  → Very Fast
O(n)      → Good
O(n log n)→ Efficient
O(n²)     → Slow for large data
O(n³)     → Very Slow
O(2ⁿ)     → Extremely Slow
O(n!)     → Practically Impossible'''