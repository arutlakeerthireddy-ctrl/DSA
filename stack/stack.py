#what is stack?
'''
A stack is a linear data structure that follows LIFO(last in first out) principle
the last element inserted into stack is removed first
All insertions and deletions operations happen only at one end called the top

'''
#Example
'''imagine a stack of books
top
30
20
10
bottom
if we remove a book 30 comes out first because it was added last
'''
#Algorithm
'''
-push(insert)
1.check if the stack is full(for fixed-size stacks)
2.increment the pointer
3.insert the new element at top
4.end
-pop(Delete)
1.check if the stack is empty
2.remove the top element
3.decrement the top pointer
4.return the removed element
-peek(Top)
1.check if the stack is empty
2.return the element at the top
3,end
'''
#operations
#push: adds an element to the top
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)#[10,20, 30]
#pop:removes the top element
stack=[10,20,30]
removed=stack.pop()
print(removed)#20
print(stack)#[10,20]
#peek(top):returns the top element without removing it
stack=[10,20,30]
print(stack[-1])#30
#isEmpty():checks whether stack is empty
stack=[]
print(len(stack)==0)#True
#isFull():used only when the stack has a fixed size
#ex:
'''
max size=5
current elements
10
20
30
40
50
stack is full
'''
#python lists grow dynamically ,so isFull() is useually not required
#size:return no. of elements
stack=[10,20,30]
print(len(stack))#3

#Types of stack
#1.static stack
'''
uses an array
fixed size
cannot grow beyond its capacity
may cause overflow if full
'''
#Example:
'''size=5
10
20
30
40
50
push(60)
overflow'''
#2.Dynamic stack
'''
uses linked lists or dynamic arrays
size can grow as needed
more memory efficient'''
#ex
10
20
30
#push 40
10
20
30
40

#Time complexity:for all operations:O(1)

#stack overflow:occurs when trying to push an element into a full stack
#stack underflow:occurs when trying to pop from empty stack

