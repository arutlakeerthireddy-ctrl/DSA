'''For every element, find the nearest greater element on its left.
Input:arr = [4,5,2,10,8]
Output:[-1,-1,5,-1,10]'''
def Near_Greater(arr):
    answer=[]
    stack=[]
    for i in range(len(arr)):#0,1,2,3,4
        current=arr[i]#4,5,2,10,8
        while stack and stack[-1]<current:#4<5,5<2,5<10,10<8
            stack.pop()#[],[]
        if stack:
            answer.append(stack[-1])#[-1,-1,5],[-1,-1,5,5,10]
        else:
            answer.append(-1)#[-1,-1],[-1,-1,5,-1]
        stack.append(current)#[4],[5],[10],[10,8]
    return answer
arr=[4,5,2,10,8]
print(Near_Greater(arr))#[-1,-1,5,-1,10]