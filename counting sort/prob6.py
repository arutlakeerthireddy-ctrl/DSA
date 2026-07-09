''' Sort Marks of Students
Marks range from 0-100.
Input:[95,81,70,95,60,81]
Output:[60,70,81,81,95,95]'''
def stable_counting_sort(arr):
    count=[0]*(max(arr)+1)
    for num in arr:
        count[num]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    output=[0]*len(arr)
    for num in reversed(arr):
        output[count[num]-1]=num
        count[num]-=1
    return output
print(stable_counting_sort([95,81,70,95,60,81]))#[60, 70, 81, 81, 95, 95]

