#find the nearest greater element on its right.
def Next_Greater(arr):
    stack=[]
    answer=[]
    for i in range(len(arr)-1,-1,-1):
        current=arr[i]
        while stack and stack[-1]<=current:
            stack.pop()
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
        stack.append(current)
    return answer[::-1]
    
arr = [4,5,2,10,8]
print(Next_Greater(arr))#[5, 10, 10, -1, -1]

#improvement
def Next_Greater(arr):
    stack=[]
    answer=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        current=arr[i]
        while stack and stack[-1]<=current:
            stack.pop()
        if stack:
            answer[i]=stack[-1]
        else:
            answer[i]=-1
        stack.append(current)
    return answer
    
arr = [4,5,2,10,8]
print(Next_Greater(arr))#[5, 10, 10, -1, -1]