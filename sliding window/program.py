#Maximum Element in Every Window of Size K
def max_window(arr,k):
    window=arr[:k]
    max_ele=[]
    max_ele.append(max(window))
    for i in range(k,len(arr)):
        window.pop(0)
        window.append(arr[i])
        max_ele.append(max(window))
    return max_ele
arr=[1,2,3,4,5]
k=3
print(max_window(arr,k))#[3, 4,5]  ....bruteforce approach
    
