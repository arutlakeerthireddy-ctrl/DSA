#what is queue
'''
queue is a linear data structure that follows fifo -first in first out
the person/item enters first will leave first'''
#example:imagine a queue at ticket counter
#Important queue terms
#front:the front is where elements are removed
#Rear:the rear is where elements are inserted
'''
front          rear
|               |
[10] [20] [30] [40]'''

#Basic queue operations(4)
'''
#enqueue()
# dequeue()
# peek/front()
# isEmpty()
'''
#enqueue:Adds an element to the rear
'''
Initially queue=[]
enqueue 10=[10]
enqueue 20=[10,20]
enqueue 30= front-[10,20,30]-rear
'''
#using deque
from collections import deque
q=deque()
q.append(10)
q.append(20)
q.append(30)
print(q)
#deque([10, 20, 30])

#Dequeue=Removes the element from the front
'''
front->[10,20,30]<-rear
dequeue:10 is removed
remain:front->[20,30]<-rear
#python:q.popleft()'''
#Example
from collections import deque
q=deque([10,20,30])
x=q.popleft()
print(x)
print(q)
#10
#deque([20, 30])

#peek/front:sometimes we dont want to remove the first element.we only want to see it,that's called peek
'''
front->[10,20,30]
peek gives 10
but 10 remains in the queue
#python:print(q[0])'''
#example
q=deque([10,20,30])
print(q[0])
print(q)
'''
10
deque([10, 20, 30])'''

#isEmpty:checks whether the queue contains elements
q=deque()
print(len(q)==0)#True
#or
if not q:
    print("queue is empty")

#complete queue
from collections import deque
q=deque()
#Enqueue
q.append(10)
q.append(20)
q.append(30)
print(q)
#peek
print('Front:',q[0])
#dequeue
print('Removed:',q.popleft())
print(q)
#isEmpty
if not q:
    print('queue is empty')
else:
    print('queue is not empty')
'''
deque([10, 20, 30])
Front: 10
Removed: 10
deque([20, 30])
queue is not empty'''

#why use deque instead of list?
q=[]
q.append(10)
q.append(20)
q.append(30)
q.pop(0)
#this works,but pop(0) is inefficient
#when the first element is removed ,python has to shift the remaining elements
#with deque:both adding and removing from the ends are efficient

#queue using list
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop(0)
print(queue)
'''
[1, 2, 3]
[2, 3]'''

#Time complexity:using deque
#Enqueue-O(1)
#Dequeue-O(1)
#peek-O(1)
#isEmpty-O(1)

#Types of queues
#1.simple queue
#2.circular queue
#3.priority queue
#4.Deque
'''
1. Queue basics
      ↓
2. Enqueue / Dequeue
      ↓
3. Queue implementation
      ↓
4. Circular Queue
      ↓
5. Deque
      ↓
6. Priority Queue
      ↓
7. Queue using Stack
      ↓
8. BFS using Queue
      ↓
9. Monotonic Queue
      ↓
10. Queue-based LeetCode problems'''


