stack=[]
stack.append('k')
stack.append('e')
stack.append('e')
stack.append('r')
print(stack)#['k', 'e', 'e', 'r']
peek=stack[-1]
print(peek)#r
stack.pop()
print(stack)#['k', 'e', 'e']
isEmpty=not bool(stack)
print(isEmpty)#False
size=len(stack)
print(size)#3

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if self.isEmpty():
            return 'stack is empty'
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return 'stack is Empty'
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
obj=Stack()
obj.push('k')
obj.push('e')
obj.push('e')
obj.push('r')
print('stack:',obj.stack)
print('peek:',obj.peek())
print('pop:',obj.pop())
print('isEmpty:',obj.isEmpty())
print('size:',obj.size())
'''
stack: ['k', 'e', 'e', 'r']
peek: r
pop: r
isEmpty: False
size: 3'''

