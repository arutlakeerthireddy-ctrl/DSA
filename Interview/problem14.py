#Find All Duplicates 
# Given an array where elements may appear more than once, find all duplicates.
arr=[2,3,4,2,6]
result=[]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
for key in freq:
    if freq[key]>1:
        result.append(key)
print(result)#[2]



