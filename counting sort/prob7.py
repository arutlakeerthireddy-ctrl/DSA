''' Sort Characters
Input:banana
Output:aaabnn
Hint: Use ASCII values.'''
def sort_characters(s):
    count=[0]*128
    for ch in s:
        count[ord(ch)]+=1
    result=""
    for i in range(len(count)):
        while count[i]>0:
            result+=chr(i)
            count[i]-=1
    return result
print(sort_characters("banana"))#aaabnn




