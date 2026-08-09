#1.For every element, find the nearest smaller element on its right.
def Next_smaller(arr):
    stack=[]
    answer=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        current=arr[i]
        while stack and stack[-1]>=current:
            stack.pop()
        if stack:
            answer[i]=stack[-1]
        else:
            answer[i]=-1
        stack.append(current)
    return answer
arr=[4,5,2,10,8]
print(Next_smaller(arr))#[2, 2, -1, 8, -1]
#Time complexity=O(n)
#space complexity=O(n)