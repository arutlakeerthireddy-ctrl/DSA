#monotonic stack:A monotonic stack is a stack that always keeps its elements in sorted(increasing or decreasing)order by popping elements that break the order
#types
#1.monotonic increasing stack
'''
elements are stored in increasing order from bottom to top
#example
bottom->1 3 5 7<-top'''
#2.monotonic decreasing stack
'''
elements are stored in decreasing order from bottom to top
#example
bottom->9 6 4 2<-top'''

#use
'''
it helps solve problems involving the next/previous greater or smaller element in O(n) time instead of O(n**2) 
by ensuring each element is pushed and popped at most once'''

#program1
def Monotonic_Inc(arr):
    stack=[]
    for i in range(len(arr)):
        current=arr[i]
        while stack and stack[-1]>current:
            stack.pop()
        stack.append(current)
    
    return stack
arr=[4,2,5,1,3]
print(Monotonic_Inc(arr))#[1,3]

#program2
def Monotonic_dec(arr):
    stack=[]
    for i in range(len(arr)):
        current=arr[i]
        while stack and stack[-1]<current:
            stack.pop()
        stack.append(current)
    return stack
arr=[4,2,5,1,3]
print(Monotonic_dec(arr))#[5,3]
#time:O(n),space:O(n)