stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)#[10, 20, 30, 40]
print(stack[-1])#40
stack.pop()
print(stack)#[10,20,30]
isEmpty=not bool(stack)
print(isEmpty)#False
size=len(stack)
print(size)#3

#stack using class
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
            return 'stack is empty'
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
obj=Stack()
obj.push(1)
obj.push(2)
obj.push(3)
print('stack:',obj.stack)
print('peek:',obj.peek())
print('pop:',obj.pop())
print('current stack:',obj.stack)
print('isEmpty:',obj.isEmpty())
print('size:',obj.size())









