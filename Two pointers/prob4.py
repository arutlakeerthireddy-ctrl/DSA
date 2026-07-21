'''Merge Two Sorted Arrays
Problem: Merge two sorted arrays into one sorted array.
Example:
Input:
A = [1,3,5]
B = [2,4,6]
Output:[1,2,3,4,5,6]'''
'''
def merge_arrays(A,B):
    arr=sorted(A+B)
    return arr
A=[1,3,5]
B=[2,4,6]
print(merge_arrays(A,B))#[1, 2, 3, 4, 5, 6]
'''
def merge_arrays(A,B):
    i=0
    j=0
    result=[]
    while i<len(A) and j<len(B):#1<3 0<3,1<3 1<3,2<3 1<3,2<3 2<3,3<3-no
        if A[i]<=B[j]: #1<2 3<2-no,3<4,5<4-no,5<6
            result.append(A[i])#[1],[1,2,3],[1,2,3,4,5]
            i+=1 #1,2,3
        elif A[i]>B[j]:#3>2,5>4
            result.append(B[j])#[1,2],[1,2,3,4]
            j+=1 #1,2
    while i<len(A):
        result.append(A[i])
        i+=1
    while j<len(B):
        result.append(B[j])
        j+=1
    
    return result
A=[1,3,5]
B=[2,4,6]
print(merge_arrays(A,B))




